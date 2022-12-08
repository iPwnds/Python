from math import sqrt

s1 = int(input("insert length of the first side: "))
s2 = int(input("insert length of the second side: "))
s3 = int(input("insert length of the third side: "))

s = (s1 + s2 + s3) / 2

formula = sqrt(s * (s - s1) * (s - s2) * (s - s3))

rounded = str(round(formula,2))

print("area of the triangle: " + rounded)
