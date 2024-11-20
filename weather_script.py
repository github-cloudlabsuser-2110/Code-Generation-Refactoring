import requests

API_KEY = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):
    """Fetch weather data for a given city."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def process_weather_data(data):
    """Process and extract relevant weather information."""
    if data:
        city = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return f"Weather in {city}: {temperature}°C, {weather_description}"
    else:
        return "Weather data not available."

def main():
    city = input("Enter city name: ")
    weather_data = fetch_weather(city)
    result = process_weather_data(weather_data)
    print(result)

if __name__ == "__main__":
    main()