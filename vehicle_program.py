# Created on 22 Nov 2016
# Created by: Matthew Lourenco
# This is a program that creates a custom vehicle

from vehicle import *

#create a vehicle
car = Vehicle()
van = Vehicle()

print('Speed: ' + str(car.speed))
car.accelerate(100)
print('Speed: ' + str(car.speed))
car.license_plate_number = 'ZZZZ777'
print('License plate number: ' + str(car.license_plate_number) + '\n')

print('Speed: ' + str(van.speed))
van.accelerate(50)
print('Speed: ' + str(van.speed))
van.brake(70)
print('Speed: ' + str(van.speed))
van.colour = 'cyan'
print('Colour: ' + str(van.colour))
