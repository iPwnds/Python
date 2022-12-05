#import tan and pi
from math import tan
from math import pi
#user input
n = int(input("insert number of sides: "))
s = int(input("insert the length of a side: "))
#formula
formula = n * s**2 / (4 * tan(pi/n))
#round the answer
rounded = str(round(formula,2))
#print the answer
print("area of the polygon: " + rounded)
