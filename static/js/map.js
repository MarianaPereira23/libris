//Map from contacts.html

var mymap = L.map('map').setView([50.105, 14.41], 14);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

//The code bellow was adapted from https://stackoverflow.com/questions/23910594/leaflet-responsive-design-creating-different-zoom-levels-for-different-screen - however this only works after refreshing the page for some reason that I don't understand yet
var width = screen.width;
if (width < 541) {
    mymap.setZoom(13);
}  else {
    mymap.setZoom(14);
}
//Here ends the code adapted from https://stackoverflow.com/questions/23910594/leaflet-responsive-design-creating-different-zoom-levels-for-different-screen

//  MAP MARKERS - code written according to Leaflet documentation 

var marker1 = L.marker([50.105, 14.41]).addTo(mymap)
   .bindPopup('<p class="content-font">Fountain Stromovka, come meet us!</p>')
    .closePopup();