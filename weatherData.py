import requests

from pprint import pprint

API_key = "1" #API KEY
url = "http://api.openweathermap.org/data/2.5/weather?"

cityName = input("Enter a city Name : ")
dataUrl = url + "appid=" + API_key + "&q=" + cityName

weatherInformation = requests.get(dataUrl).json()

print("Current Weather Data Of " + cityName +":\n")

pprint(weatherInformation)