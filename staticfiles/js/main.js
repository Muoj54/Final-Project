// static/js/main.js
document.addEventListener('DOMContentLoaded', (event) => {
    mapboxgl.accessToken = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA';

    try {
        const jsonData = document.getElementById('location-data').textContent.trim();
        const locationData = JSON.parse(jsonData);
        const busStops = locationData.bus_stops;

        if (busStops && Array.isArray(busStops) && busStops.length > 0) {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        const userLat = position.coords.latitude;
                        const userLng = position.coords.longitude;

                        var map = new mapboxgl.Map({
                            container: 'map',
                            style: 'mapbox://styles/mapbox/streets-v11',
                            center: [userLng, userLat],
                            zoom: 12
                        });

                        new mapboxgl.Marker().setLngLat([userLng, userLat]).setPopup(new mapboxgl.Popup().setHTML("Your Location")).addTo(map);

                        busStops.forEach(stop => {
                            new mapboxgl.Marker({ color: 'red' })
                                .setLngLat([stop.longitude, stop.latitude])
                                .setPopup(new mapboxgl.Popup().setHTML(stop.name))
                                .addTo(map);
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
        } else {
            console.error('No bus stops found or bus_stops is not an array.');
            alert('No bus stops found.');
        }
    } catch (error) {
        console.error('Error parsing location data', error);
    }
});
