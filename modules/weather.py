import requests

convert_celsius = lambda x: float(str(float(x) - 272)[:3])


def getWeather():
    class weather:
        def __init__(self, res):
            self.temp = convert_celsius(res["main"]["temp"])
            self.feeling_temp = convert_celsius(res["main"]["feels_like"])
            self.wind = res["wind"]["speed"]
            self.condition = res["weather"][0]["description"]

    api_key = "81a76b93a5fd803b592f303b7b3b1ede"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Istanbul"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    res = requests.get(complete_url)
    w = weather(res.json())
    res = ('{} is {}, temperature is {}°C and feels like {}°C degree. The wind speed is {} knot/s.'.format(
        city_name, w.condition, w.temp, w.feeling_temp, w.wind))
    return res
