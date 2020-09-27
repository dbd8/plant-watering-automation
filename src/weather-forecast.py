import requests
import datetime


def rain_in_next_timewindow(weather_data, time_window) -> bool:
    current_time = datetime.datetime.now()

    for hours in range(len(weather_data["hourly"])):
        if (datetime.datetime.fromtimestamp(
                weather_data["hourly"][hours]["dt"]) - current_time).total_seconds() <= time_window * 3600:
            if weather_data["hourly"][hours]["weather"][0]["main"] == "Rain":
                print(datetime.datetime.fromtimestamp(weather_data["hourly"][hours]["dt"]))
                print(weather_data["hourly"][hours]["weather"][0]["description"])
                return True

    return False


time_window = 12

lat = "49.2627"
lon = "9.2995"
exclude = "current,minutely,daily"
api_key = "XXX"

open_weather_map_url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=%s&appid=%s" % (
    lat, lon, exclude, api_key)

r = requests.get(open_weather_map_url)

weather_data = r.json()

# print(weather_data)
print(rain_in_next_timewindow(weather_data, time_window))
