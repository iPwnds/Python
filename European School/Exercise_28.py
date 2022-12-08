#user input
height = float(input("insert height(in m): "))
weight = float(input("insert weight(in kg): "))

#BMI formula
BMI  = weight/(height * height)

#round the answer
rounded = str(round(BMI,2))

#print BMI
print("your BMI is: " + rounded)
