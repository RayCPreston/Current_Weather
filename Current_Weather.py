# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:01:16 2020

@author: Ray
"""

import json
import requests
import sys

def kelvinToFarenheit(kelvin) -> float:
    return (((kelvin - 273.15) * 9) / 5) + 32

url = "http://api.openweathermap.org/data/2.5/weather?q=houston&appid=11993438e7010c0b046d71c38fc3b3b9"
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

forecast = weatherData["weather"]

print("The forecast today is " + forecast[0]["description"])

#get the min max and feels like temperature
temps = weatherData["main"]
maxTemp = format(kelvinToFarenheit(temps["temp_max"]), ".1f")
print("The high today is " + maxTemp + "\N{DEGREE SIGN}")
minTemp = format(kelvinToFarenheit(temps["temp_min"]), ".1f")
print("The low today is " + minTemp + "\N{DEGREE SIGN}")
currentTemp = format(kelvinToFarenheit(temps["temp"]), ".1f")
print("The cuurent temperature is " + currentTemp + "\N{DEGREE SIGN}")
feelsLike = format(kelvinToFarenheit(temps["feels_like"]), ".1f")
print("But it feels like " + feelsLike + "\N{DEGREE SIGN}")




'''
print("Current weather in houston", end = " ")

#print(weather)

weatherMain = weather["weather"][0]

print(weatherMain)
'''


