import os
import requests
from dotenv import load_dotenv

# Load ENV
load_dotenv()

# Constants
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = os.getenv("WEATHER_API_URL")
GEO_API_URL = os.getenv("GEO_API_URL")

def get_weather_data(place, days=1):

    # Get Longitude and Latitude

    latitude, longitude = get_location_data(place)
    if latitude is None or longitude is None:
        return None
    else:
        weather_response = requests.get(f"{WEATHER_API_URL}?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}&units=metric")
        filtered_data = weather_response.json()["list"]
        nr_values = 8 * days
        filtered_data = filtered_data[:nr_values]
        return filtered_data


def get_location_data(place):
    try:
        geo_response  = requests.get(f"{GEO_API_URL}?q={place}&limit=1&appid={WEATHER_API_KEY}")
        lat = geo_response.json()[0]["lat"]
        lon = geo_response.json()[0]["lon"]
    except IndexError:
        return None, None
    else:
        return lat, lon

if __name__ == "__main__":
    # latit, longit = get_location_data("London")
    get_weather_data("London", days=3, kind="Temperature")
    get_weather_data("London", kind="Sky")