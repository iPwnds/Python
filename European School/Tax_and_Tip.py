#Question: The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values are displayed using two decimal places.
#Criteria: Exercise 6: Tax and Tip (solved, 17 Lines)

import random

Price = random.uniform(0, 100)
roundedPrice = round(Price, 2)
print('The price of your meal is: ' + str(roundedPrice))

Tip = 1.18
print('The default tip is: ' + str(Tip))

Tax = random.uniform(1.10, 1.17)
roundedTax = round(Tax, 2)
print('The default tax in Luxemburg is: ' + str(roundedTax))

Total = Price * Tip * Tax
roundedTotal = round(Total, 2)

print(roundedTotal)