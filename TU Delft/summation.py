import sys

my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]  # Fill this list to test the implementations!

def sum_A(l):
    prev = sys.maxsize
    s = 0
    for i in range(len(l)):
        if (l[i] < prev):
            prev = l[i]
            s += l[i]
    return s


def sum_B(l):
    prev = sys.maxsize
    s = 0
    for i in range(len(l)):
        if (l[i] < prev):
            prev = l[i]
            s += l[i]
    return sum(l)
    

def sum_C(l):
    prev = sys.maxsize
    s = 0
    for i in range(len(l)):
        if (l[i] < prev):
            prev = l[i]
        s += l[i]
    return s


def sum_D(l):
    s = 0
    for i in range(len(l)):
        if (l[i] > 0):
            s += l[i]
    return s


def sum_E(l):
    s = 0
    if len(l) == 0:
        return -1
    for i in range(len(l)):
        s += l[i]
    return s


print("Implementation A", sum_A(my_list))
print("Implementation B", sum_B(my_list))
print("Implementation C", sum_C(my_list))
print("Implementation D", sum_D(my_list))
print("Implementation E", sum_E(my_list))