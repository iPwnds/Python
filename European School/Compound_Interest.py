#Question: Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places.
#Criteria: Exercise 9: Compound Interest (19 Lines)

Interest = 1.04
Deposit = input('How much would you like to deposit: \n')
Deposit = int(Deposit)

Total1 = Deposit * Interest
Total2 = Total1 * Interest
Total3 = Total2 * Interest

Total1 = round(Total1, 2)
Total2 = round(Total2, 2)
Total3 = round(Total3, 2)

Total1 = str(Total1)
Total2 = str(Total2)
Total3 = str(Total3)

print('Your savings account after 1 year: ' + Total1)
print('Your savings account after 2 year: ' + Total2)
print('Your savings account after 3 year: ' + Total3)