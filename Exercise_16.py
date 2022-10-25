#import pi from math
from math import pi

#user input
radius = int(input("insert radius: "))

#formula
areaCircle = pi * radius**2
volumeCircle = 4/3 * pi * radius**3

#round the answers
rounded1 = round(areaCircle, 2)
rounded2 = round(volumeCircle, 2)

#print the rounded answers
print("the area of the circle is: " + str(rounded1))
print("the volume of the circle is: " + str(rounded2))
