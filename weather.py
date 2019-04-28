import requests
import json

import board
import neopixel

# API key (example)
API_key = "0123456789abcdef9876543210fedcba"
# X coordinate
x_coordinate = "40.7104"
# Y coordinate
y_coordinate = "-74.0167"
# temperature units (defaults to based on geographic location)
units = "auto"

# set GPIO pin here
pixels = neopixel.NeoPixel(board.D18, 40, brightness=0.1)

def displayWeatherOnLED(temperature):
    pixels.fill((0, 0, 0))
    tens = (int(temperature/10)) * 2
    ones = (int(temperature%10)) * 2
    for LEDones in range(0, ones, 2):
        # set color for ones place here
        pixels[LEDones] = (255, 0, 0)
    for LEDtens in range(0, tens, 2):
        # set color for tens place here
        pixels[LEDtens+ones] = (0, 255, 0)
    return
 
requestString = "https://api.darksky.net/forecast/" + API_key + "/" + x_coordinate + "," + y_coordinate + "?units=" + units

response = requests.get(requestString)

x = response.json() 

y = x["currently"]
current_temperature = y["temperature"]

displayWeatherOnLED(int(current_temperature))
