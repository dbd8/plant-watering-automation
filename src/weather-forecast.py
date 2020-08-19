import requests

lat = "49.2627"
lon = "9.2995"
exclude = "current,minutely,daily"
api_key = "6e28081a2602523329de6d510710dd1f"

open_weather_map_url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=%s&appid=%s" % (
    lat, lon, exclude, api_key)

r = requests.get(open_weather_map_url)

weather_data = r.json()

print(weather_data)
