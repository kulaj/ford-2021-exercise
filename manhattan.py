'''
Manhattan Distance Calculator
Created by Justin Kula on 3/13/2021
'''

from collections import namedtuple
# The decimal type is used to help avoid floating point errors on display
from decimal import Decimal

# Define a type that will be used for points
Point = namedtuple('Point', ['x', 'y'])

def compute_manhattan_distance(p1, p2):
    '''
    Input is two Points, p1 and p2
    The manhatten distance is computed, and returned as a float
    '''
    return abs(p1.x-p2.x)+abs(p1.y-p2.y)

def is_numeric(s):
    '''
    Returns True if it is possible to convert the provided string as a decimal,
    and False otherwise
    '''
    try:
        Decimal(s)
        return True
    except:
        return False

def input_variable(variable):
    '''
    This function initiates an input loop to prompt the user to enter a numeric value.
    The input gathering process is repeated until the value inputted is numeric
    Input 'variable' is the name of the variable being requested.
    '''
    n = None
    while not n:
        n = input(variable+"-value: ")
        if not is_numeric(n):
            print("Invalid value for", variable, "- Please enter a numeric value")
            n = None
    return Decimal(n)

def input_yn(message):
    '''
    This function initiates an input loop to prompt the user to enter a y/n value.
    The input gathering process is repeated until the value inputted is y or n
    Input 'message' is the question to ask the user
    '''
    v = None
    while not v:
        v = input(message).lower()
        if not v in ["y","n"]:
            print("Invalid input - Please enter either 'y' (yes) or 'n' (no)")
            v = None
    return v

def input_point(name):
    '''
    This function receives a Point as input from the console,
    using the input helper functions defined above
    '''
    print("Beginning Input for Point:", name, "(x,y)")
    x = input_variable("x")
    y = input_variable("y")
    return Point(x,y)


# begin main sequence
if __name__ == '__main__':
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