import requests

# Send GET request to the OpenWeatherMap API
url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"
response = requests.get(url)
response_data = response.json()

# Test latitude and longitude
assert response_data['coord']['lat'] == 51.51, "Latitude is incorrect"
assert response_data['coord']['lon'] == -0.13, "Longitude is incorrect"

# Additional test cases
# 1. Check if the response has a 'name' property with the value 'London'
assert response_data['name'] == "London", "City name is incorrect"

# 2. Check if the response has a 'sys' property with a 'country' property and the value 'GB'
assert response_data['sys']['country'] == "GB", "Country is incorrect"

# 3. Check if the response has a 'weather' property, and the weather description is not empty
assert response_data['weather'][0]['description'] != "", "Weather description is empty"

# Print a success message if all tests pass
print("All tests passed!")
