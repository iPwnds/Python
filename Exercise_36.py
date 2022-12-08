userInput = int(input("insert number of human years: "))

x = 21
formula = x + (userInput - 2) * 4
formula2 = userInput * 10.5

if userInput > 2:
    print("equivalent dog years: " + str(formula))
if userInput == 2:
    print("equivalent dog years: 21")
if  -1 < userInput < 2:
    print("equivalent dog years: " + str(formula2))
if userInput < 0:
    print("cannot insert negative number")
