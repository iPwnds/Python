#import sqrt
from math import sqrt

#variables
d = int(input("enter height: "))
a = 9.81
v0 = 0

#formula
finalSpeed = str(sqrt(v0**2 +2 * a * d))

#print answer
print("final speed: " + finalSpeed)
