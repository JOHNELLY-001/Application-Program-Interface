async function sendMessage(message) {
    const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    });

    const data = await response.json();
    return data.response;
}

// Example usage
sendMessage('yeah').then(response => {
    console.log('Bot response:', response);
});