import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather():
    print("\n*** Get current weather condition! ***")
    city = input("\nPlease enter your city name: ")
    

    request_url = 'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    print(request_url)

get_current_weather()