p1 = [3, 9] # Point 1 here.
p2 = [4, 8] # Point 2 here.


def invalidInput(p,q):
    if (len(p) < 2):
        return "List p1 is too short"
    if (len(q) < 2):
        return "List p2 is too short"
    if (p[0] == q[0] and p[1] == q[1]):
        return "The points are equal"
    if (p[0]-q[0] == 0 or p[1] - q[1] == 0):
        return "Can not compute horizontal or vertical line"
    return None
    
def A(p,q):
    inv = invalidInput(p,q)
    if (inv):
        return inv
    a = (p[1]-q[1])*1.0/(q[0]-p[0])
    b = (p[1] -a*p[0])
    return "y = " + str(round(a,1)) + "x + " + str(round(b,1))
    
def B(p,q):
    inv = invalidInput(p,q)
    if (inv):
        return inv
    a = (p[0]-q[0])*-1.0/(q[1]-p[1])
    b = (p[0] -a*p[1])
    return "x = " + str(round(a,1)) + "y + " + str(round(b,1))
    
def C(p,q):
    inv = invalidInput(p,q)
    if (inv):
        return inv
    a = (p[0]-q[0])*-1.0/(q[1]-p[1])
    b = 1/((p[0]-q[0])*1.0/(q[1]-p[1]))
    c = (p[0] -a*q[0])
    return str(round(a,1)) + "y + " + str(round(b,1)) + "x + " + str(round(c,1)) + " = 0"

def D(p,q):
    inv = invalidInput(p,q)
    if (inv):
        return inv
    a = (p[0]-q[0])*-1.0/(q[1]-p[1])
    b = 1/((p[0]-q[0])*1.0/(q[1]-p[1]))
    c = -(q[0] -p[1])
    return str(round(a,1)) + "y + " + str(round(b,1)) + "x + " + str(round(c,1)) + " = 0"

def E(p,q):
    inv = invalidInput(p,q)
    if (inv):
        return inv
    a = (p[1]-q[1])*1.0/(p[0]-q[0])
    b = (p[1] -a*p[0])
    return "y = " + str(round(a,1)) + "x + " + str(round(b,1))
    

print("Implementation A:", A(p1,p2))
print("Implementation B:", B(p1,p2))
print("Implementation C:", C(p1,p2))
print("Implementation D:", D(p1,p2))
print("Implementation E:", E(p1,p2))