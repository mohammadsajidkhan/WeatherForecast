import requests
import json 
import sys


def get_weather(city):
    api_key = "bc16d91560e37d9cb15f19dc9606e15d"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params= params)

    data = json.loads(response.text)

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"Weather Forecast for {city}:")
        print(f"Temperature: {temperature} C")
        print(f"Humidity {humidity}%")
        print(f"Description {description}:")
    
    else:
        print(f"Error: {data['message']}")

# To check if city name was provided as a CLI arg

if len(sys.argv) >1:
    city_name = " ".join(sys.argv[1:])
    print(city_name)
    get_weather(city_name)
else:
    print("Please provide a valid city name")

