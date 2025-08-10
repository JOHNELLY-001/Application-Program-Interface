import requests

API_KEY = "your_key"
city = "Arusha"
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

# send GET request to the API
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Extract temperature
temperature = data['main']['temp']
print(f'The current temperature in {city} is {temperature}')