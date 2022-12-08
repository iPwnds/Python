#import math function
import math

#user input
year = int(input("insert year: "))

year1 = str(year)
#variables
a = math.remainder(year,19)
b  = year // 100  
c = math.remainder(year,100)
d = b // 4
e = math.remainder(b,4)
f = (b+8)//25
g = (b-f+1)//3
h = math.remainder((19*a+b-d-g+15),30)
i = c // 4
k = math.remainder(c,4)
l = math.remainder(32 + 2*e + 2*i - h - k,7)
m = (a + 11*h + 22*l)//(45*l)

month = str((h + l - 7*m + 114)//31) 
day =str(1 + math.remainder(h + l - 7*m + 114,31))

#print answer
print("date of Easter: " + day + "/" + month + "/" + year1)
