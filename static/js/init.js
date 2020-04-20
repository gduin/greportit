$(function(){
	//alert('OK');
	var options = {
  					enableHighAccuracy: true,
  					timeout: 5000,
  					maximumAge: 0
				};

	if(navigator.geolocation)
	{
		navigator.geolocation.getCurrentPosition(getCoords, getError, options);
	}
	else
	{
		initialize(10.082446,-69.31366);
	}

	function getCoords(position)
	{
		var lat= position.coords.latitude;
		var lng= position.coords.longitud;
		
		initialize(lat, lng);
	}

	function getError(err)
	{
		//console.warn('ERROR(' + err.code + ') ' + err.message);
		initialize(10.082446,-69.31366);
	}

	function initialize(lat, lng)
	{
		var latlng = new google.maps.LatLng(lat, lng);
		var mapSettings={
			center: latlng,
			zoom:15,
			streetViewControl:false,
			mapTypeId: google.maps.MapTypeId.SATELLITE
			/*disableDefaultUI: true,
			scaleControl: true,
			rotateControl: true,
			panControl: true,*/	
			/*ROADMAP*/
		};

		map=new google.maps.Map($('#mapa').get(0),mapSettings);

		var marker= new google.maps.Marker({
			position:latlng,
			map:map,
			draggable:true,
			title:'Colocame'
		});

		
		google.maps.event.addListener(map, 'click',function(event){
			marker.setPosition(event.latLng);
		});

		google.maps.event.addListener(marker,'position_changed', function(){
			getMarkerCoords(marker);			
		});	
	}
	

	function getMarkerCoords(marker)
	{
		var markerCoords= marker.getPosition();
		$('#id_lat').val(markerCoords.lat());
		$('#id_lng').val(markerCoords.lng());
		//alert(markerCoords);
	}

	//$('#id_imagenes').change(test);
	<!--**********************************************-->
	//var data = {};

//function createReaderHandler(name) {
//  return function(ev) {
//    data[name] = ev.target.result;
//    console.log(data);
//  };
//}

//function test(ev) {
//  var files = ev.target.files; // FileList object

  // Loop through the FileList
//  for (var i = 0; i < files.length; i++) {
//    var file = files[i],
//        name = file.name || file.fileName,
//        reader = new FileReader();

//    reader.onload = createReaderHandler(name);
//    reader.readAsText(file);
//  }
//}
	<!--**********************************************-->

	$('#form_report').submit(function(e){

		var formObj = $(this);
    	var formURL = formObj.attr("action");
    	var formData = new FormData(this);
		e.preventDefault();
		console.log($(this).serialize());
		fdata=$(formData).serialize();
		console.log(fdata);
		/*
		$.ajax({
        	url: formURL,
    		type: 'POST',
        	data:  data,
    		mimeType:"multipart/form-data",
    		contentType: false,
        	cache: false,
        	processData:false,
    		success: function(data)
    		{
 				$('#data').html(data.msg);
				$('#form_report').each(function(){ this.reset(); });
    		},
     		error: function(data) 
     		{
     			alert(data.msg);
     		}          
    	});*/

		$.ready(function() {
			
		});
		
		$.post('/report/save/', $(this).serialize(),function(data){
			if(data.ok)
			{
				$('#data').html(data.msg);
				$('#form_report').each(function(){ this.reset(); });
			}
			else
			{
				alert(data.msg);
			}
		},'json');

	});
	
});