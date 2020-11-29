# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:01:16 2020

@author: Ray
"""

import json
import requests
import sys


url = "http://api.openweathermap.org/data/2.5/weather?q=houston&appid=11993438e7010c0b046d71c38fc3b3b9"
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
print(weatherData)

weather = weatherData["weather"]
print(weather)
print(weather[0]["main"])


'''
print("Current weather in houston", end = " ")

#print(weather)

weatherMain = weather["weather"][0]

print(weatherMain)
'''


