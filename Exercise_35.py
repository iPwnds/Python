#import remainder
from math import remainder

#user input
num = float(input("insert number: "))

#if statement
if remainder(num,2) == 0:
    result = "the number is even"
else:
    result = "the number is odd"

#print result
print(result)
