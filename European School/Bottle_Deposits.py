#Question: In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. In one particular jurisdiction, drink containers holding one liter or less have a SO.10 deposit, and drink containers holding more than one liter have a $0.25 deposit. Write a program that reads the number of containers of each size from the user. Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and two digits to the right of the decimal point.
#Criteria: Exercise 5: Bottle Deposits (solved, 15 Lines)

Amount = int(input("How many drink containers do you have: \n"))
Capacity = float(input("What are the size's of the drink containers (in litres): \n"))
Total = 0

if Capacity <= 1:
    Refund = 0.10

if Capacity > 1:
    Refund = 0.25

Total = Amount * Refund

Rounded = round(Total, 2)

print('You will recieve: $' + str(Rounded) + ' for these drink containers')