#Question: Create a program that reads two integers, a and b, from the user. Your program should compute and display: The sum of a and b, The difference when b is subtracted from a, The product of a and b, The quotient when a is divided by b, The remainder when a is divided by b, The result of log10 a, The result of a^b
#Criteria: Exercise 10: Arithmetic (solved, 22 Lines)

import math #importing the math library

a = input("input a number: \n") #getting the first number
b = input("input a number: \n") #getting the second number
a = int(a) #converting from string to integer
b = int(b) #converting from string to integer

one = a + b #the first value
two = b - a #the second value
three = a * b #the third value
four = a / b #the fourth value
five = a % b #the fifth value
six = math.log10(a) #the sixth value
seven = a ** b #the seventh value

print(one) #printing the first value
print(two) #printing the second value
print(three) #printing the third value
print(four) #printing the fourth value
print(five) #printing the fifth value
print(six) #printing the sixth value
print(seven) #printing the seventh value