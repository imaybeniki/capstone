function initialiseMap(rows) {
	var startInfoWindow = new google.maps.InfoWindow();
	var endInfoWindow = new google.maps.InfoWindow();

	for(var i = 0; i < rows.length; i++) {
		(function () {
			var markerObject = {
				id: rows[i]['id'],
				name: rows[i]['name'],
				weight: rows[i]['weight'],
				marker: null,
				markerImage: null,
				color: null,
				points: -1
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
				position: {lat: rows[i]['lat'], lng: rows[i]['long']},
				map: map,
				icon: new google.maps.MarkerImage(markerImage)
			});
			marker.startContent = '<h1>' + rows[i]['name'] + '</h1>' +
				'<div><p>' + rows[i]['lat'] + ', ' + rows[i]['long'] + '</p>' +
				'<p>' + rows[i]['weight'] + ' / ' + rows[i]['capacity'] + '</p>' +
				'<a href="javascript:startPointProcess()">Start here</a>' +
				'</div>';

			markerObject.marker = marker;
			markerObject.markerImage = markerImage;
			google.maps.event.addListener(marker, 'click', function(e) {
			    if(!pointMode) {
                    startMarker = markerObject;
                    startInfoWindow.setContent(marker.startContent);
                    startInfoWindow.open(map, this);
                } else if(marker != startMarker.marker) {
			        endInfoWindow.setContent(marker.endContent);
			        endInfoWindow.open(map, this);
                }
			});
			markerList[markerObject.id] = markerObject;
		}());
	}
	google.maps.event.trigger(map, "resize");
}

function startPointProcess() {
    // Update startMarker's infoWindow TODO
    
	// Get point list since we have marker
	var pointList = makeFakeListOfNodes(markerList);

	// Populate markers
	populatePoints(pointList);
}

function populatePoints(listOfNodes) {
	pointMode = true;
	for(var i = 0; i < listOfNodes.length; i++) {
		if(startMarker.id != listOfNodes[i].id) {
            (function () {
                var currMarker = markerList[listOfNodes[i].id];
                currMarker.points = listOfNodes[i].points;
                currMarker.marker.setIcon(markerImages[currMarker.color][currMarker.points.toString()]);
                currMarker.marker.endContent = '<h1>' + currMarker.name + '</h1>' +
                    '<div><p>You would earn ' + currMarker.points + ' points!</p>' +
                    '<a>Go here</a>' +
                    '</div>';
            }());
        }
	}
}

function resetPoints() {
	for(var i = 0; i < markerList.length; i++) {
		markerList[i].marker.setIcon(markerList[i].markerImage);
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
	for(var i = 1; i <= maxPoints; i++) {
		images['green'][i.toString()] = baseDir + i + "_green.png";
	}
	// Yellow
	for(var i = 1; i <= maxPoints; i++) {
		images['yellow'][i.toString()] = baseDir + i + "_yellow.png";
	}
	// Red
	for(var i = 1; i <= maxPoints; i++) {
		images['red'][i.toString()] = baseDir + i + "_red.png";
	}

	return images;
}