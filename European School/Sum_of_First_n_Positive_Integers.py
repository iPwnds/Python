#Question: Write a program that reads a positive integer, n, from the userand then displays the sum of all of the integers from 1 to n. The sum of the first n positive integers con be computed using the formula: sum = (n)(n + 1) / 2
#Criteria: Exercise 7: Sum of First n Positive Integers (solved, 11 Lines)

y = input('Enter a positive number: \n')
y = int(y)

x = y + 1

if y >= 0:
    sum = y * x / 2
    print('The sum is: ' + str(sum))

else:
    print('Please enter a positive value.')