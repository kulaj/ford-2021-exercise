from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def compute_manhattan_distance(p1, p2):
    return abs(p1.x-p2.x)+abs(p1.y-p2.y)

def is_numeric(s):
    try:
        float(s)
        return True
    except:
        return False

def input_variable(variable):
    n = None
    while not n:
        n = input(variable+"-value: ")
        if not is_numeric(n):
            print("Invalid value for", variable, "- Please enter a numeric value")
            n = None
    return float(n)

def input_yn(message):
    v = None
    while not v:
        v = input(message).lower()
        if not v in ["y","n"]:
            print("Invalid input - Please enter either 'y' (yes) or 'n' (no)")
            v = None
    return v

def input_point(name):
    print("Beginning Input for Point:", name, "(x,y)")
    x = input_variable("x")
    y = input_variable("y")
    return Point(x,y)

print("-----Welcome to Manhattan Distance Calculator by Justin Kula, 2021-----\n")
while True:
    p1 = input_point("p1")
    print("\n")
    p2 = input_point("p2")
    result = compute_manhattan_distance(p1,p2)
    print("\nManhattan Distance Result:", result, "\n")
    yn = input_yn("Would you like to compute another? (y/n): ")
    if yn == "n":
        break
    else:
        print("\n")

print("\nThank you for using the calculator!")