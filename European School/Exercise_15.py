#user input
userInput = int(input("measurement in feet: "))
#conversion
inches = str(userInput * 12)
yards = str(userInput // 3)
miles = str(userInput // 5280)
#print answers
print("inches: " + inches)
print("yards: " + yards)
print("miles: " + miles)
