#user input
m = int(input("input mass of water (in grams): "))
T = int(input("input temperature change(in °C: "))

#heat capacity of water
C = 4.186

#formula
q = m * C * T
kWh = q * 0.000000277777778
cost = kWh * 8.9

#print answer
print("cost: " + cost)
