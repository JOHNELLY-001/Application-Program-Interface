// const url = 'http://127.0.0.1:8000/api'

// async function apiCast() {
//     try{
//         const response = await fetch(url);

//         if (!response) {
//             alert ("Network problems!");
//             return;
//         }

//         const result = await response.json();

//         console.log(result);

//     } catch (error) {
//         console.error(error);
//     }
// }

// apiCast()

const url = 'http://localhost:3000/users';

document.getElementById('userForm').addEventListener('submit', async function (e) {
  e.preventDefault(); // Prevent form from refreshing page

  const userData = {
    name: document.getElementById('name').value.trim(),
    email: document.getElementById('email').value.trim(),
    password: document.getElementById('password').value.trim()
  };

  formPost(userData); // ✅ Pass the data correctly
});

async function formPost(userData) {
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(userData)
  };

  try {
    const response = await fetch(url, options);

    if (!response.ok) {
      const errorData = await response.json();
      alert(`Error: ${errorData.error || 'Something went wrong'}`);
      return;
    }

    const result = await response.json();
    alert(`User ${result.name} registered successfully!`);
    return result;

  } catch (error) {
    console.error('Network error:', error);
    alert('Network error. Please try again.');
  }
}





// const url = 'http://127.0.0.1:8000/api';

// async function fetchData() {
//     try {
//         const response = await fetch(url, {
//             method: 'GET',
//             mode: 'no-cors',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//         });

//         if (!response.ok) {
//             throw new Error(`HTTP error! Status: ${response.status}`);
//         }

//         const data = await response.json();
//         console.log('Data received:', data);
//         // displayData(data);  // Call displayData to render the data
//     } catch (error) {
//         console.error('Error fetching data:', error);
//     }
// }

// // Function to display data on HTML page
// function displayData(data) {
//     const container = document.getElementById('data-container');  // Fix typo here

//     // Clear any existing content
//     container.innerHTML = '';

//     // Loop through the data and create HTML elements
//     data.forEach(item => {
//         const itemDiv = document.createElement('div');
//         itemDiv.className = 'data-item';

//         itemDiv.innerHTML = `
//             <h2>${item.name}</h2>
//             <p><b>Description:</b> ${item.description}</p>
//             <img src="${item.image}" alt="${item.name} Image">
//             <video controls>
//                 <source src="${item.media}" type="video/mp4">
//                 Your browser does not support the video tag.
//             </video>
//             <p><b>Link:</b> <a href="${item.link}" target="_blank">${item.link}</a></p>
//             <p><b>Contact:</b> ${item.contact}</p>
//         `;

//         // Append the item to the container
//         container.appendChild(itemDiv);
//     });
// }

// Call the function
// fetchData();