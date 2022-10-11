#Question: In the United States, fuel efficiency for vehicles is normally expressed in miles-per-gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100km). Use your research skills to determine how to convert from MPG to L/100km. Then create a program that reads a value from the user in American units and displays the equivalent fuel efficiency in Canadian units.
#Criteria: Exercise 11: Fuel Efficiency (13 Lines)

US = input("Miles per gallon: \n") #asking the user for input

US = int(US) #converting from string to integer

conversion = 235.215 / US #doing the math

conversionround = round(conversion, 2) #rounding it down to 2 numbers

conversionround = str(conversionround) #converting from float to string

print("this is the formula used to calculate the final result: 235.215/MPG") #explaining the math 

print("Fuel efficiency from MPG to L/100KM is: " + conversionround) #printing the final result