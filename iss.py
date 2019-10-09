#!/usr/bin/env python
# just was able to work on it
# __author__ = 'Swavae with some help from Zach'

import json
import turtle 
import urllib.request
import time
import requests

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

# screen = turtle.Screen()
# screen.setup(720, 360)
# screen.setworldcoordinates(-180, -90, 180, 90)
# screen.bgpic('map.gif')

# screen.register_shape('iss.gif')
# iss = turtle.Turtle()
# iss.shape('iss.gif')
# iss.setheading(90)

# iss.penup()
# iss.goto(lon, lat)

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


def data_collector():
    crew = requests.get('http://api.open-notify.org/astros.json')
    dictionary = crew.text
    dictionary = json.loads(dictionary)
    for person in dictionary['people']:
        print('{} is on the ISS orbiting the Earth'.format(
            person['name']))

def get_position():
    pos = requests.get(
        'http://api.open-notify.org/iss-now.json')
    positioning = pos.text
    positioning = json.loads(positioning)
    current_pos = positioning['iss_position']
    print('At ' + str(time.ctime(positioning['timestamp'])) +
          ' the ISS was at ' + str(current_pos['longitude']) +
          ' latitude and ' + str(current_pos['latitude']) + ' longitude')
    return (float(current_pos['longitude']), float(current_pos['latitude']))

def indy_pass():
    r = requests.get(
        "http://api.open-notify.org/iss-pass.json?lat=40&lon=-86.1349")
    is_over = r.text
    is_over = json.loads(is_over)
    over_indy = is_over['response'][0]
    next_pass = time.ctime(over_indy['risetime'])
    return 'The ISS will pass over Indy next at: {}'.format(next_pass)

def burgle_turts(iss_position, next_pass):
    new_screen = turtle.Screen()
    new_screen.bgpic('./map.gif')
    new_screen.addshape('iss.gif')
    new_screen.setup(width=720, height=360)
    new_screen.setworldcoordinates(-180, -90, 180, 90)
    new_var = turtle.Turtle()
    new_var.shape('iss.gif')
    new_var.penup()
    new_var.goto(iss_position)
    indy_dot = turtle.Turtle()
    indy_dot.shape('circle')
    indy_dot.color('yellow')
    indy_dot.penup()
    indy_dot.goto(-86.1349, 40.273502)
    msg = turtle.Turtle()
    msg.color('yellow')
    msg.write(next_pass, True, align='center', font=('Arial', 25, 'normal'))
    new_screen.exitonclick()

def main():
    data_collector()
    pos = get_position()
    next_pass = indy_pass()
    burgle_turts(pos, next_pass)
if __name__ == '__main__':
    main()
