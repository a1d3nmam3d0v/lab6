import os
from datetime import datetime
from pprint import pprint

import requests

url = "http://api.openweathermap.org/data/2.5/forecast"
key = os.environ.get("WEATHER_KEY")


def main():
    city = get_city()
    country = get_country_code()
    city_comma_country = city + "," + country
    all_weather_data = get_weather_data(city_comma_country, key)
    show_4cast(all_weather_data)


def get_city():
    city = input("City? ")
    return city


def get_country_code():
    country_code = input("Country? ").strip()
    return country_code


def get_weather_data(location, key):
    query = {"q": location, "units": "imperial", "appid": key}
    response = requests.get(url, params=query)
    data = response.json()
    return data


def show_4cast(weather_data):
    for data in weather_data["list"]:
        temp = data["main"]["temp"]

        wind_speed = data["wind"]["speed"]

        timestamp = data["dt"]
        date_time = datetime.fromtimestamp(timestamp)
        # PART 2  - I didn't see this question until now so I didn't know we had to choose MN or UTC time
        # I never liked the way timestamps are formatted so I looked up a way to change it and found this strftime method
        date = date_time.strftime("%x")  # "locale's appropriate date"
        time = date_time.strftime("%X")  # "locale's appropriate  time"

        weather_key_list = weather_data["list"][0]["weather"]
        description = (item["description"] for item in weather_key_list)
        # spent like all day tryna figure out how to access 'description' in the json lol
        # with this "generator expression" (stackoverflow) was the closest i got
        # but then i realized its only accessing the first description in the json over n over
        # which makes sense cuz of the [0] but idk and so tired of trying!
        for i in description:
            print(
                f"On {date} at {time}, the temp will be {temp}F, possibly {i}, with a wind speed of {wind_speed}."
            )


main()
