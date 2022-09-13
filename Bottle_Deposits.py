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