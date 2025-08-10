async function fetchMovieCast() {
    const url = 'https://imdb236.p.rapidapi.com/imdb/tt7631058/cast';
    const options = {
        method: 'GET',
        headers: {
            'x-rapidapi-key': '2969c31982msh16c5f8cd679e4afp111087jsndbf46414398d',
            'x-rapidapi-host': 'imdb236.p.rapidapi.com'
        }
    };

    try {
        const response = await fetch(url, options);
        const result = await response.json(); 
        console.log(result); // Debug: Check the API response in console

        // Get the UL element where cast will be displayed
        const castList = document.getElementById('castList');
        castList.innerHTML = ''; // Clear previous data

        // Loop through the array and create list items
        result.forEach(actor => {
            const listItem = document.createElement('li');
            listItem.textContent = `${actor.fullName} - ${actor.job} (Roles: ${actor.characters.join(', ')})`;
            castList.appendChild(listItem);
        });

    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

fetchMovieCast(); // Call the function