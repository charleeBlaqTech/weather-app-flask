
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city):
   
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data= requests.get(request_url).json();
    return weather_data


if __name__ == "__main__":
    print(f'\n*** Get current Weather conditions ☁☁☁ ***\n')

    city= input("\nPlease enter a city name:\n")
    weather_data= get_current_weather(city)
    pprint(weather_data);