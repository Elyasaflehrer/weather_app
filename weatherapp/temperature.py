import datetime
from datetime import timedelta
import requests
from data_weather import DataWeather
import os
import json

secret_keys = "secret_keys.json"
with open(secret_keys, 'r') as f:
    api_keys = json.loads(f.read())
API_KEY = api_keys["API_KEY"]


def get_dict_7_days(location):
    coordinates = get_coordinates(location)
    if coordinates is None:
        return None
    return get_dict_for_7_days(coordinates.get("lat"), coordinates.get("lon"))


def get_coordinates(location):
    req = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&appid={API_KEY}")

    if len(req.json()) == 0:
        return None
    req_dict = dict(req.json()[0])
    print("req_dict['country']", req_dict["country"])
    return {"lat": req_dict.get("lat"), "lon": req_dict.get("lon")}


def get_dict_for_7_days(lat, lon):
    part = "current,minutely,hourly,alerts"
    daily_weather = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_KEY}&units=metric")
    daily_weather_dict = daily_weather.json()

    location_dict = dict()
    for i in range(0, 7):
        curr = daily_weather_dict["daily"][i]  # ["temp"]
        icon = curr["weather"][0]["icon"]
        description = curr["weather"][0]["description"]
        wind_speed = daily_weather_dict["daily"][i]["wind_speed"]
        icon = f'http://openweathermap.org/img/wn/{icon}@2x.png'
        location_dict[i] = DataWeather(get_name_day(i), curr["temp"]["day"],
                                       curr["temp"]["night"], curr["humidity"], icon, description, wind_speed,
                                       get_date(i))
    return location_dict


def get_name_day(index_day):
    dt = datetime.datetime.today() + timedelta(days=index_day)
    day = dt.day
    year = dt.year
    month = dt.month
    intDay = datetime.date(year, month, day).weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[intDay]


def get_date(index_day):
    date = datetime.datetime.today() + timedelta(days=index_day)
    return date.strftime("%d/%m/%Y")
