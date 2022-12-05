#user input
seconds = int(input("insert number of seconds: "))
#variables
days = 86400
hours = 3600
minutes = 60
second = 1
#formulas
d  = str(seconds // days)
seconds = seconds%86400
h = str(seconds // hours)
seconds = seconds%3600
m = str(seconds // minutes)
seconds = seconds%60
s = str(seconds // second)
seconds = seconds%1
#print answer
print(d + ":" + h + ":" + m + ":" + s )
