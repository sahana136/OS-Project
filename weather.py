import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Gulbarga&appid=3e75bdf3a5195839560620a811280383'
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description