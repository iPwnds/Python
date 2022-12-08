#user input
input1 = int(input("insert feet: "))
input2 = int(input("insert inches: "))
#convert to inches and then to cm
total = input1 * 12 + input2
centimetres = total * 2.54
#round the answer
rounded = str(round(centimetres, 2))
#print the answer
print("your height in centimetres is: " + rounded)
