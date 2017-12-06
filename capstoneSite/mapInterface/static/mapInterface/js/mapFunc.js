var startInfoWindow;
var endInfoWindow;

var markerList = {};
var pointMode = false;
var startMarker;

var map;

// TODO format info windows
// TODO better implement a user friendly interface for interacting with nodes

/**
 * Initialises map data (markerList, startInfoWindow, endInfoWindow)
 *
 * @param rows
 */
function initialiseMap(rows) {
    // Init InfoWindows
	startInfoWindow = new google.maps.InfoWindow();
	endInfoWindow = new google.maps.InfoWindow();

	// For each row in table
	for(var i = 0; i < rows.length; i++) {
		(function () {
		    // Init marker object
			var markerObject = {
				id: rows[i]['id'],
				name: rows[i]['name'],
				weight: rows[i]['weight'],
                capacity: rows[i]['capacity'],
                lat: rows[i]['lat'],
                long: rows[i]['long'],
				marker: null,
				markerImage: null,
				color: null,
				points: -1,
                startContent: null,
                endContent: null
			};
			var markerImage;

			// Select marker image from flag
			if(rows[i]['flag'].trim() === 'G') {
				markerImage = greenMarker;
				markerObject.color = 'green';
			} else if(rows[i]['flag'].trim() === 'Y') {
				markerImage = yellowMarker;
				markerObject.color = 'yellow';
			} else {
				markerImage = redMarker;
				markerObject.color = 'red';
			}

			// Create marker
			var marker = new google.maps.Marker({
				title: rows[i]['name'],
				position: {lat: markerObject.lat, lng: markerObject.long},
				map: map,
				icon: new google.maps.MarkerImage(markerImage)
			});

			// Create startContent for info window
			markerObject.startContent = '<h1>' + markerObject.name + '</h1>' +
				'<div><p>' + markerObject.lat + ', ' + markerObject.long + '</p>' +
				'<p>' + markerObject.weight + ' / ' + markerObject.capacity + '</p>' +
				'<a onclick="startPointProcess()" href="#">Start here</a>' +
				'</div>';

			markerObject.marker = marker;
			markerObject.markerImage = markerImage;

			// Create listener
			google.maps.event.addListener(marker, 'click', function(e) {
			    if(!pointMode) {
                    startMarker = markerObject;
                    startInfoWindow.setContent(markerObject.startContent);
                    startInfoWindow.open(map, this);
                } else if(marker != startMarker.marker) {
			        endInfoWindow.setContent(markerObject.endContent);
			        endInfoWindow.open(map, this);
                }
			});
			markerList[markerObject.id] = markerObject;
		}());
	}
	google.maps.event.trigger(map, "resize");
}

/**
 * Function to start the point process
 */
function startPointProcess() {
    // Update startMarker's infoWindow
    startMarker.startContent = '<h1>' + startMarker.name + '</h1>' +
            '<div><p>' + startMarker.lat + ', ' + startMarker.long + '</p>' +
            '<p>' + startMarker.weight + ' / ' + startMarker.capacity + '</p>' +
            '<a onclick="endPointProcess()" href="#">Cancel</a>' +
            '</div>';
    startInfoWindow.setContent(startMarker.startContent);

	// Get point list since we have marker
    var pointList = requestPoints(startMarker.id);
}

/**
 * Function to populate marker's images with points values and update endContent
 *
 * @param {Array} listOfNodes
 */
function populatePoints(listOfNodes) {
    // Start point boolean
	pointMode = true;

	// Loop through list
	for(var i = 0; i < listOfNodes.length; i++) {
		if(startMarker.id != listOfNodes[i].id) {
            (function () {
                var currMarker = markerList[listOfNodes[i].id];
                currMarker.points = listOfNodes[i].points;
                currMarker.marker.setIcon(markerImages[currMarker.color][currMarker.points.toString()]);
                currMarker.endContent = '<h1>' + currMarker.name + '</h1>' +
                    '<div><p>You would earn ' + currMarker.points + ' points!</p>' +
                    '<a onclick="addPointsAndEndPointProcess(' +
                    currMarker.points + ', ' + currMarker.lat + ', ' + currMarker.long +
                        ')" href="#">Go here</a>' +
                    '</div>';
                console.log(currMarker.endContent);
            }());
        }
	}
}

/**
 * Function to make AJAX request to get_points view in Django
 *
 * @param {Number} id
 */
function requestPoints(id) {
    $.ajax({
        url: '/ajax/get_points/',
        data: {
            'id': id,
            'size': Object.keys(markerList).length,
        },
        dataType: 'json',
        success: function(data) {
            populatePoints(data.points);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus); alert("Error: " + errorThrown);
        }
    });
}

/**
 * Function to make AJAX request to update_user_points in Django. Also updates the user's distance field
 *
 * @param {Number} points
 * @param {float} lat
 * @param {float} long
 */
function sendPoints(points, lat, long) {
    $.ajax({
        url: '/ajax/update_user_points/',
        data: {
            'points': points,
            'lat1': startMarker.lat,
            'long1': startMarker.long,
            'lat2': lat,
            'long2': long
        },
        dataType: 'json',
        success: function(data) {
            alert(data.message);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus); alert("Error: " + errorThrown);
        }
    });
}

/**
 * Function to add points to a user and end the point process
 *
 * @param {Number} points
 * @param {float} lat
 * @param {float} long
 */
function addPointsAndEndPointProcess(points, lat, long) {
    endPointProcess();
    sendPoints(points, lat, long);
}

/**
 * Function to end the point process
 */
function endPointProcess() {
    // End point boolean
	pointMode = false;
	resetPoints(); // Reset points
	startInfoWindow.close();
	endInfoWindow.close();

	startMarker.startContent = '<h1>' + startMarker.name + '</h1>' +
            '<div><p>' + startMarker.lat + ', ' + startMarker.long + '</p>' +
            '<p>' + startMarker.weight + ' / ' + startMarker.capacity + '</p>' +
            '<a onclick="startPointProcess()" href="#">Start here</a>' +
            '</div>';
}

/**
 * Function to reset point markers to standard markers
 */
function resetPoints() {
	for(var key in markerList) {
		markerList[key].marker.setIcon(markerList[key].markerImage);
	}
}

/**
 * Function to make a fake list of nodes for testing
 *
 * @param markers
 * @returns {Array}
 */
function makeFakeListOfNodes(markers) {
	var outList = [];
	var counter = 2;
	var keyList = Object.keys(markers);
	for(var i = 0; i < keyList.length; i++) {
		if(startMarker.id != keyList[i]) {
            (function () {
                var tempNode = {
                    id: keyList[i],
                    points: counter
                }
                counter = counter + 1;
                if (counter > 9) {
                    counter = 2;
                }
                outList.push(tempNode);
            }())
        }
	}
	return outList;
}

/**
 * Function to create marker images object.
 *
 * @param {String} baseDir
 * @returns {{green: {}, yellow: {}, red: {}}}
 */
function createMarkerImageObject(baseDir) {
	var maxPoints = 9;
	var images = {
		green: {},
		yellow: {},
		red: {}
	};
	// Green
	for(var i = 0; i <= maxPoints; i++) {
		images['green'][i.toString()] = baseDir + i + "_green.png";
	}
	// Yellow
	for(var i = 0; i <= maxPoints; i++) {
		images['yellow'][i.toString()] = baseDir + i + "_yellow.png";
	}
	// Red
	for(var i = 0; i <= maxPoints; i++) {
		images['red'][i.toString()] = baseDir + i + "_red.png";
	}

	return images;
}