#from math import pi
from math import pi

#user imput radius and height
radius = int(input("insert radius: "))
height = int(input("insert height: "))

#formula
area = pi * radius**2
total = area * height

#round and print rounded answer
rounded = str(round(total,1))
print("volume: " + rounded)
