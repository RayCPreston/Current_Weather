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

weather = json.loads(response.text)

print("Current weather in houston")

wList = weather["list"]

print(wList[0]["weather"][0]["main"], '-', wList[0]['weather'][0]['description'])