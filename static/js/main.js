// static/js/main.js
document.addEventListener('DOMContentLoaded', (event) => {
    mapboxgl.accessToken = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA';

    let map, userLat, userLng, selectedBusStop;

    function calculateRoute() {
        if (!selectedBusStop || !userLat || !userLng) return;

        const url = `https://api.mapbox.com/directions/v5/mapbox/driving/${userLng},${userLat};${selectedBusStop.longitude},${selectedBusStop.latitude}?geometries=geojson&access_token=${mapboxgl.accessToken}`;
        
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const route = data.routes[0].geometry;
                const routeCoordinates = route.coordinates;

                const routeLayer = {
                    id: 'route',
                    type: 'line',
                    source: {
                        type: 'geojson',
                        data: {
                            type: 'Feature',
                            properties: {},
                            geometry: route
                        }
                    },
                    layout: {
                        'line-join': 'round',
                        'line-cap': 'round'
                    },
                    paint: {
                        'line-color': '#7DF9FF',
                        'line-width': 5,
                        'line-opacity': 0.75
                    }
                };

                if (map.getLayer('route')) {
                    map.getSource('route').setData(routeLayer.source.data);
                } else {
                    map.addLayer(routeLayer);
                }

                const instructions = data.routes[0].legs[0].steps.map(step => step.maneuver.instruction);
                document.getElementById('instructions').innerHTML = `<ol>${instructions.map(i => `<li>${i}</li>`).join('')}</ol>`;
            })
            .catch(error => console.error('Error fetching route data:', error));
    }

    try {
        const jsonData = document.getElementById('location-data').textContent.trim();
        const locationData = JSON.parse(jsonData);
        const destinationName = locationData.destination;
        const busStops = locationData.bus_stops;

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    userLat = position.coords.latitude;
                    userLng = position.coords.longitude;

                    map = new mapboxgl.Map({
                        container: 'map',
                        style: 'mapbox://styles/mapbox/streets-v11',
                        center: [userLng, userLat],
                        zoom: 12
                    });

                    new mapboxgl.Marker().setLngLat([userLng, userLat]).setPopup(new mapboxgl.Popup().setHTML("Your Location")).addTo(map);

                    busStops.forEach(stop => {
                        const marker = new mapboxgl.Marker({ color: 'red' })
                            .setLngLat([stop.longitude, stop.latitude])
                            .setPopup(new mapboxgl.Popup().setHTML(stop.name))
                            .addTo(map);

                        marker.getElement().addEventListener('click', () => {
                            selectedBusStop = stop;
                            calculateRoute();
                        });
                    });
                },
                (error) => {
                    console.error('Error getting user location', error);
                    alert('Unable to retrieve your location');
                }
            );
        } else {
            console.error('Geolocation not supported by this browser.');
            alert('Geolocation not supported by this browser.');
        }
    } catch (error) {
        console.error('Error parsing location data', error);
    }
});
