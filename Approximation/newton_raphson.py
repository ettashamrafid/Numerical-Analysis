import math

def func(x):
    return pow(x,3) - 2*pow(x,2) + 3*x -4

def derivative(x):
    return 3*pow(x,2) - 4*x + 3


def newton_raphson(x_i):
    x_next= x_i - (func(x_i)/derivative(x_i))
    if abs(x_next-x_i)<1e-6:
        return x_next
    else:
        return newton_raphson(x_next)
    
print(newton_raphson(3))