import datetime as dt 
import requests 

BASE_URL ="https://api.openweathermap.org/data/2.5/weather?"

API_KEY= open('keys.txt','r').read()

CITY="Växjö"

def kelvein_to_celsius_farenheit(kelvin):
    celsuis= kelvin -273.15
    farenheit = celsuis *(9/5) *32 
    return celsuis,farenheit



url = BASE_URL +"appid=" +API_KEY+"&q=" + CITY 
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_farenheit = kelvein_to_celsius_farenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_farenhiet = kelvein_to_celsius_farenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity =response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

print(f"Temperatue in {CITY}:{temp_celsius:.2f}")
print(f"Temperatue in {CITY} feels like:{feels_like_celsius:.2f}")
print(f"Humidty in {CITY}: {humidity}%")
print(f"Wind speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")
print(f" Sun rises in {CITY} at {sunrise_time} local time")
print(f" Sun set in {CITY} at {sunset_time} local time")