
hexo.extend.tag.register('googleMap', function (args) {
  var map;
  function initMap() {

    var myLatLng = [];
    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 8
    });

    var myLatLng = {lat: -25.363, lng: 131.044};
    var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      title: 'Hello World!'
    });
  }
});
