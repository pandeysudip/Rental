function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}

//function for dropdown menu and initial graphs 
function init() {
    d3.json('/data/all_data').then((data) => {
        //select the dropdown.
        var menu = d3.select("#selDataset");
        console.log(data)

        //states.filter(onlyUnique)
        var zipcodes = []
        for (let i = 0; i < 5000; i++) {
            c = data[i].houseZip
            zipcodes.push(c);
        }
        var uniqueZip = zipcodes.filter(onlyUnique)
        uniqueZip.forEach((zip) => {
            menu.append("option").text(zip).property("value", zip);
        });
        //creating function for initial plots 
        var initSample = uniqueZip[1]
        createMap(initSample);
    })
};

function createMap(commodity) {
    //removing map if already exist
    var container = L.DomUtil.get('map');
    if (container != null) {
        container._leaflet_id = null;
    }

    // Define a markerSize() function that will give each city a different radius based on its population.
    function markerSize(value) {
        return Math.sqrt(value) * 1;
    }

    d3.json('/data/all_data').then((data) => {
        var cMarkers = []
        for (var i = 0; i < data.length; i++) {
            var d = data[i]
            console.log(d);


            console.log(d.lat);
            if (d.Commodity == commodity) {


                // Setting the marker 
                cMarkers.push(
                    L.circle([d.lat, d.lng], {
                        color: "blue",
                        fillColor: "green",
                        fillOpacity: 0.75,
                        radius: markerSize(d.rentAmount)

                    }).bindPopup(`<h1>${d.houseZip}</h1>  <hr> <h3>Rent:$ ${d.rentAmount.toLocaleString()}</h3>`)
                )

            }
        }
        var zipdata = L.layerGroup(cMarkers);

        // Create the tile layer that will be the background of our map.
        var streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        });

        //google satellite
        googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
            maxZoom: 20,
            subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
        });

        // Create a baseMaps object to hold the streetmap layer.
        var baseMaps = {
            "Street Map": streetmap,
            "Google Sat": googleSat
        };

        // Create an overlay object to hold our overlay.
        var overlayMaps = {
            Zipcode: zipdata
        };

        // Create our map, giving it the streetmap and earthquakes layers to display on load.
        var myMap = L.map("map", {
            center: [
                32.6, -117.0
            ],
            zoom: 10,
            layers: [streetmap, zipdata]
        });

        // Add the layer control to the map.
        L.control.layers(baseMaps, overlayMaps, {
            collapsed: false
        }).addTo(myMap);

    })

};

function optionChanged(newSample) {
    createMap(newSample);
};

init();