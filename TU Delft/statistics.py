import sys


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 1, 1]  # Fill this list to test the implementations!


def impl_A(l):
    if (len(l) == 0):
        return "empty list"
    prev = l[0]
    l.sort()
    s = 0
    h = 1
    a = 0
    for i in range(1,len(l)):
        if (l[i] > prev):
            if (h>=a):
                s = prev*1.0
                a = h
            h = 0
            prev = l[i]
        h += 1
    if (h>=a):
        s = prev*1.0
        
    return round(s,1)


def impl_B(l):
    if (len(l) == 0):
        return "empty list"
    prev = l[0]
    l.sort()
    s = 0
    h = 1
    a = 0
    for i in range(1,len(l)):
        if (l[i] > prev):
            if (h>a):
                s = prev*1.0
                a = h
            h = 0
        prev = l[i]
        h += 1
    if (h>a):
        s = prev*1.0
    return round(s,1)


def impl_C(l):
    if (len(l) == 0):
        return "empty list"
    prev = sys.maxsize
    l.sort()
    s = 0
    for i in range(len(l)):
        if (l[i] < prev):
            prev = l[i]
        s += l[i]*1.0/len(l)
    return round(s,1)


def impl_D(l):
    if (len(l) == 0):
        return "empty list"
    prev = sys.maxsize
    l.sort()
    s = 0
    for i in range(len(l)):
        if (l[i] < prev):
            prev = l[i]
        s += l[i]*1.001/len(l)
    return round(s,1)


def impl_E(l):
    if (len(l) == 0):
        return "empty list"
    l.sort()
    s = 0
    for i in range(len(l)):
        if (len (l) % 2 == 1):
            s = (l[int(len(l)/2)])*1.0
        else:
            s = (l[int(len(l)/2.0 - 1)] + l[int(len(l)/2.0)]) / 2.0
    return round(s,1)
    

print("Implementation A", impl_A(my_list))
print("Implementation B", impl_B(my_list))
print("Implementation C", impl_C(my_list))
print("Implementation D", impl_D(my_list))
print("Implementation E", impl_E(my_list))