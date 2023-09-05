
let apiKey = 'fdf2e5d92bd32f089135e21a9a5d504f';

function fetchWeatherData(city) {
    return new Promise((resolve, reject) => {
        let lat, lon;

        if(city === "mumbai") {
            lat = 19.0760;
            lon = 72.8777;
        } else if(city === "delhi") {
            lat = 28.6139;
            lon = 77.2090;
        } else if(city === "goa") {
            lat = 15.2993;
            lon = 74.1240;
        } else {
            reject('Unsupported city');
            return;
        }

        const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}`;

        fetch(url)
        .then(response => {
            if (!response.ok) {
                reject('Network response was not ok');
            } else {
                return response.json();
            }
        })
        .then(data => {
            resolve(data);
        })
        .catch(error => {
            reject(error);
        });
    });
}

function getWeather() {
    let dropdown = document.getElementById('cityDropdown');
    let city = dropdown.value;

    fetchWeatherData(city)
    .then(data => {
        document.getElementById('weatherData').innerHTML = `Temperature in ${city}: ${data.main.temp}K, Condition: ${data.weather[0].description}`;
    })
    .catch(error => {
        console.error('There was a problem:', error);
        document.getElementById('weatherData').innerHTML = 'Error fetching weather data.';
    });
}