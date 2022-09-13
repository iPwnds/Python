Types = input("How many different drink container size's do you have: \n")

Types = int(Types)

Amounts = []
Capacities = []
Refund = []
Totals = []

for i in range(0, Types):
    Amount = int(input("How many drink containers do you have: \n"))
    Capacity = float(input("What are the size's of the drink containers (in litres): \n"))

    Amounts.append(Amount)
    Capacities.append(Capacity)

if Types == 1:
    if Capacities[0] <= 1:
        Refund = 0.10

    if Capacities[0] > 1:
        Refund = 0.25

    Totals[0] = Amounts[0] * Refund[0]

    Total = Totals[0]

if Types == 2:
    if Capacities[0] <= 1:
        Refund = 0.10

    if Capacities[0] > 1:
        Refund = 0.25

    Totals[0] = Amounts[0] * Refund[0]

    if Capacities[1] <= 1:
        Refund = 0.10

    if Capacities[1] > 1:
        Refund = 0.25

    Totals[1] = Amounts[1] * Refund[1]

    Total = Totals[0] + Totals[1]

if Types == 3:
    if Capacities[0] <= 1:
        Refund = 0.10

    if Capacities[0] > 1:
        Refund = 0.25

    Totals[0] = Amounts[0] * Refund[0]

    if Capacities[1] <= 1:
        Refund = 0.10

    if Capacities[1] > 1:
        Refund = 0.25

    Totals[1] = Amounts[1] * Refund[1]

    if Capacities[2] <= 1:
        Refund = 0.10

    if Capacities[2] > 1:
        Refund = 0.25

    Total[2] = Amounts[2] * Refund[2]

    Total = Totals[0] + Totals[1] + Totals[2]

if Types == 4:
    if Capacities[0] <= 1:
        Refund = 0.10

    if Capacities[0] > 1:
        Refund = 0.25

    Totals[0] = Amounts[0] * Refund[0]

    if Capacities[1] <= 1:
        Refund = 0.10

    if Capacities[1] > 1:
        Refund = 0.25

    Totals[1] = Amounts[1] * Refund[1]

    if Capacities[2] <= 1:
        Refund = 0.10

    if Capacities[2] > 1:
        Refund = 0.25

    Total[2] = Amounts[2] * Refund[2]

    if Capacities[3] <= 1:
        Refund = 0.10

    if Capacities[3] > 1:
        Refund = 0.25

    Totals[3] = Amounts[3] * Refund[3]

    Total = Totals[0] + Totals[1] + Totals[2] + Totals[3]

if Types == 5:
    if Capacities[0] <= 1:
        Refund = 0.10

    if Capacities[0] > 1:
        Refund = 0.25

    Totals[0] = Amounts[0] * Refund[0]

    if Capacities[1] <= 1:
        Refund = 0.10

    if Capacities[1] > 1:
        Refund = 0.25

    Totals[1] = Amounts[1] * Refund[1]

    if Capacities[2] <= 1:
        Refund = 0.10

    if Capacities[2] > 1:
        Refund = 0.25

    Total[2] = Amounts[2] * Refund[2]

    if Capacities[3] <= 1:
        Refund = 0.10

    if Capacities[3] > 1:
        Refund = 0.25

    Totals[3] = Amounts[3] * Refund[3]

    if Capacities[4] <= 1:
        Refund = 0.10

    if Capacities[4] > 1:
        Refund = 0.25

    Totals[4] = Amounts[4] * Refund[4]

    Total = Totals[0] + Totals[1] + Totals[2] + Totals[3] + Totals[4]

Rounded = round(Total, 2)

print('You will recieve: $' + str(Rounded) + ' for these drink containers')



