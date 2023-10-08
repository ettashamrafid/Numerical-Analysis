import math

def func(x):
    return pow(x,3) - 2*pow(x,2) + 3*x -4

def secant(x_i, x_prev):
    derivative= (func(x_i)- func(x_prev))/(x_i-x_prev)
    x_next= x_i - (func(x_i)/derivative)
    if abs(x_i-x_next)<1e-6:
        return x_i
    else:
        return secant(x_next,x_i)
    

print(secant(1.5,2))