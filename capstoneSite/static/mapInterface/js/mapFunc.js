function initialiseMap(rows, map) {
	var markerList = [];
	var infoWindow = new google.maps.InfoWindow();
	
	for(var i = 0; i < rows.length; i++) {
		(function () {
			var markerImage;
			if(rows[i]['flag'] === 'G') {
				markerImage = greenMarker;
			} else if(rows[i]['flag'] === 'Y') {
				markerImage = yellowMarker;
			} else {
				markerImage = redMarker;
			}
			var marker = new google.maps.Marker({
				title: rows[i]['name'],
				position: {lat: rows[i]['lat'], lng: rows[i]['long']},
				map: map,
				icon: new google.maps.MarkerImage(markerImage)
			});
			var infoString = '<h1>' + rows[i]['name'] + '</h1>' +
				'<div><p>' + rows[i]['lat'] + ', ' + rows[i]['long'] + '</p>' +
				'<p>' + rows[i]['weight'] + ' / ' + rows[i]['capacity'] + '</p>' + 
				'</div>';
			google.maps.event.addListener(marker, 'click', function(e) {
				infoWindow.setContent(infoString);
				infoWindow.open(map, this);
			});
			markerList.push(marker);
		}());
	}
	google.maps.event.trigger(map, "resize");
}