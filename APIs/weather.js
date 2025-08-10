
// async function weatherApi() {
//     const days = document.getElementById('num-days').value;
//     const options = {
//         mode: 'no-cors'
//     }

//     if (!days) {
//         alert("Please enter number of days to forecast");
//         return;
//     }
    
//     const response = await fetch(`http://127.0.0.1:5000/predict?days=${days}`,
//         {
//             method: 'GET',
//             mode: 'no-cors',
//             headers: {
//                 'Content-Type' : 'application/json'
//             }
//         },
//     );

//     const result = await response.arrayBuffer()
//     console.log(result);

//     if (result.error) {
//         alert(result.error);
//         return;
//     };

//     // display
//     const container = document.getElementById('data-container');

//     container.innerHTML = '';

//     // create a div for each item in the data
    
//         const div = document.createElement('div');
//         div.innerHTML = `
//             <p>${result.date}</p>
//             <p>${result.temperature}</p>
//             <p>${result.weather}</p>
//             <p>${result.outfit}</p>
//             <p>${result.precaution}</p>
//             <hr>
//         `;
//         container.appendChild(div);

    
// }

// weatherApi()

async function getWeather() {
    const apiKey = '7b55810cbbcb496899c104156250905'; // Ensure you provide your API key here.
    const location = 'Singida';

    try {
        const response = await fetch(`https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${location}`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(`Temperature in ${data.location.name}: ${data.current.temp_c}C`);
    } catch (error) {
        console.error('Error fetching weather data:', error.message);
    }
}

getWeather();
