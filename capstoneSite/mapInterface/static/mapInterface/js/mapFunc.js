var startInfoWindow;
var endInfoWindow;

// TODO format info windows
// TODO better implement a user friendly interface for interacting with nodes

function initialiseMap(rows) {
	startInfoWindow = new google.maps.InfoWindow();
	endInfoWindow = new google.maps.InfoWindow();

	for(var i = 0; i < rows.length; i++) {
		(function () {
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
			var marker = new google.maps.Marker({
				title: rows[i]['name'],
				position: {lat: markerObject.lat, lng: markerObject.long},
				map: map,
				icon: new google.maps.MarkerImage(markerImage)
			});
			markerObject.startContent = '<h1>' + markerObject.name + '</h1>' +
				'<div><p>' + markerObject.lat + ', ' + markerObject.long + '</p>' +
				'<p>' + markerObject.weight + ' / ' + markerObject.capacity + '</p>' +
				'<a onclick="startPointProcess()" href="#">Start here</a>' +
				'</div>';

			markerObject.marker = marker;
			markerObject.markerImage = markerImage;
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
	//var pointList = makeFakeListOfNodes(markerList);

	// Populate markers DONE IN AJAX REQUEST
	//populatePoints(pointList);
}

function populatePoints(listOfNodes) {
	pointMode = true;
	for(var i = 0; i < listOfNodes.length; i++) {
		if(startMarker.id != listOfNodes[i].id) {
            (function () {
                var currMarker = markerList[listOfNodes[i].id];
                currMarker.points = listOfNodes[i].points;
                currMarker.marker.setIcon(markerImages[currMarker.color][currMarker.points.toString()]);
                currMarker.endContent = '<h1>' + currMarker.name + '</h1>' +
                    '<div><p>You would earn ' + currMarker.points + ' points!</p>' +
                    '<a onclick="addPointsAndEndPointProcess(' + currMarker.points + ')" href="#">Go here</a>' +
                    '</div>';
                console.log(currMarker.endContent)
            }());
        }
	}
}

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

function sendPoints(points) {
    $.ajax({
        url: '/ajax/update_user_points/',
        data: {
            'points': points,
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

function addPointsAndEndPointProcess(points) {
    endPointProcess();
    sendPoints(points);
}

function endPointProcess() {
	pointMode = false;
	resetPoints();
	startInfoWindow.close();
	endInfoWindow.close();

	startMarker.startContent = '<h1>' + startMarker.name + '</h1>' +
            '<div><p>' + startMarker.lat + ', ' + startMarker.long + '</p>' +
            '<p>' + startMarker.weight + ' / ' + startMarker.capacity + '</p>' +
            '<a onclick="startPointProcess()" href="#">Start here</a>' +
            '</div>';
}

function resetPoints() {
	for(var key in markerList) {
		markerList[key].marker.setIcon(markerList[key].markerImage);
	}
}

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