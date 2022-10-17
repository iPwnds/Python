#variables
penny = 1
nickel = 5
dime = 10
quarter = 25
loonie = 100
toonie = 200

#input user
userInput = int(input("number of cents: \n"))

print("amount of cents: " + str(userInput))

#print answer
print(userInput//200, "toonie(s)")

userInput = userInput%200

print(userInput//100, "loonie(s)")

userInput = userInput%100

print(userInput//25, "quarters")

userInput = userInput%25

print(userInput//10, "dimes")

userInput = userInput%10

print(userInput//5, "nickles")

userInput = userInput%5

print(userInput//1, "pennies")