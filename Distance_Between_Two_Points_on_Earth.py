#Question: The surface of the Earth is curved, and the distance between degrees of longitude varies with latitude. As a result, finding the distance between two points on the surface of the Earth is more complicated than simply using the Pythagorean theorem. Let (f1, g1) and (f2, g2) be the latitude and longitude of two points on the Earth's surface. The distance between these points, following the surface of the Earth, in kilometers is: distance = 6371.01 x arccos(sin(t1) x sin(g2) + cos(t1) x cos(t2) x cos(g1 - g2)) Create a program that allows the user to enter the latitude and longitude of two points on the Earth in degrees. Your program should display the distance between the points, following the surface of the earth, in kilometers.
#Criteria: Exercise 12: Distance Between Two Points on Earth (27 Lines)

from numpy import * #importing numpy for the COMPLEX math

lat1 = input("insert the latitude of point one in degrees: \n") #getting the latitude of the first point
lon1 = input("insert the longitude of point one in degrees: \n") #getting the longitude of the first point
lat2 = input("insert the latitude of point two in degrees: \n") #getting the latitude of the second point
lon2 = input("insert the longitude of point two in degrees: \n") #getting the longitude of the second point

lat1 = float(lat1) #converting the lat to a float
lon1 = float(lon1) #converting the lon to a float
lat2 = float(lat2) #converting the lat to a float
lon2 = float(lon2) #converting the lon to a float

one = sin(lat1) #the first value
two = sin(lat2) #the second value
three = cos(lat1) #the third value
four = cos(lat2) #the fourth value
five = cos(lat2 - lon2) #the fifth value

math = one * two + three * four * five #adding everything up

dis = 6371.01 * arcsin(math) #putting math in the final formula 

disr = round(dis, 2) #rounding it down to two numbers

disr = str(disr) #converting the distance to a string

print("The distance in KM is: " + disr + "KM") #printing the final result