import random

intro = input('Welcome, this is a random number generator\npress enter to start\n')

a = input('What would your lowest possible value be: \n')

b = input('What would your highest possible value be: \n')

a = float(a)

b = float(b)

random = random.randint(a, b)

print(random)