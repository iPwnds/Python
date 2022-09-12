Width = input("Width of the field (feet): \n")
Length = input("Length of the field (feet): \n")

Width = float(Width)
Length = float(Length)

print('Width of field in feet: ' + str(Width))
print('Length of field in feet: ' + str(Length))

formula = Width * Length / 43560
rounded = round(formula, 3)

print("The farmer's field is " + str(rounded) + ' acres')

print('Math done: ' + str(Width) + ' * ' + str(Length) + ' / 43560')