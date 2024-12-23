from geopy.geocoders import Photon
import os
from dotenv import load_dotenv
load_dotenv()


def get_coordinates(city, country):
    try:
        geolocator = Photon(user_agent=os.getenv("GEOPY_USER_AGENT"))
        location = geolocator.geocode(f"{city}, {country}")
        if location:
            return (location.longitude, location.latitude)
        return None
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None


def get_city(longitude, latitude):
    try:
        geolocator = Photon(user_agent=os.getenv("GEOPY_USER_AGENT"))
        location = geolocator.reverse((latitude, longitude),language='en')
        if location:
            return location._address.split(",")[0]
        return None
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

