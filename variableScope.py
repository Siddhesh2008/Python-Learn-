#variable scope= the region of a program where a variable is recognized.
#scope resolution= the process of finding the value of a variable name.
#(LEGB) local, enclosing, global, built-in

def func1():
    x = 10  # Local variable       #functions cannot see inside other functions, but they can see variables in the global scope.
    print("Inside func1, x =", x)

def func2():
    x = 20  # Local variable
    print("Inside func2, x =", x)

#Global scope
x=3
print("Inside global scope, x =", x)
func1()  # Output: Inside func1, x = 10
func2()  # Output: Inside func2, x = 20

#in-built
from math import e
e=3
print("The value of e is:", e)  # Output: The value of e is: 3

#if e is declared in the global scope, it will override the built-in value of e.
#  However, if e is not declared in the global scope, the built-in value will be used.

