import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_coordinates(city, state, country):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={API_KEY}')
    response.raise_for_status()
    data = response.json()
    return data[0]['lat'], data[0]['lon']


def get_weather_data(lat, lon):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial')
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    lat, lon = get_coordinates("San Jose", "California", "US")
    print(lat, lon)
    weather_data = get_weather_data(lat, lon)
    print(weather_data['weather'][0]['description'])
    print(weather_data['main']['temp'])
