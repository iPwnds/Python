#user input
P = int(input("insert pressure (in Pascals): "))
V = int(input("insert volume (in Liters): "))
TinC = int(input("insert temperature (in °C): "))
#variable R
R = int(8.314)
#convert from Celsius to Kelvin
T = int(TinC) + 273.15
#formula
n = P*V / R*T
#round answer
rounded = str(round(n,2))
#print answer
print("answer: " + rounded + " moles")
