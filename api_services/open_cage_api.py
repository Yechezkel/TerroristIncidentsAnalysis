import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_coordinates(city, country):
    api_key = os.getenv("OPENCAGE_API_KEY")
    url = os.getenv("OPENCAGE_API_URL")
    query = f"{city}, {country}"
    params = {"q": query, "key": api_key,  "language": "en", "pretty": 1}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data['results']:
            coordinates = data['results'][0]['geometry']
            return  coordinates['lng'], coordinates['lat']
        else:
            return "No results found."
    except requests.RequestException as e:
        return f"Error occurred: {e}"

def get_city(longitude, latitude):
    api_key = os.getenv("OPENCAGE_API_KEY")
    url = os.getenv("OPENCAGE_API_URL")
    query = f"{latitude}, {longitude}"
    params = {"q": query, "key": api_key, "language": "en", "pretty": 1}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data['results']:
            city = data['results'][0]['components'].get('city', "Unknown")
            country = data['results'][0]['components'].get('country', "Unknown")
            return city, country
        else:
            return "No results found."
    except requests.RequestException as e:
        return f"Error occurred: {e}"



