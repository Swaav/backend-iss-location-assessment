#!/usr/bin/env python
# HAVE NOT STARTED THIS YET
__author__ = '???'

import json
import turtle 
import urllib.request
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('people in space: ', result['number'])

people = result['people']
print(people)

for p in people: 
    print(p['name'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print (result)

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

#spaceCenter(HOUSTON)
lat = 29.5502
lon = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

over = result['response'][1]['risetime']
# print(over)

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)


def main():
    pass


if __name__ == '__main__':
    main()
