import math
def func(x):
    #return (4*pow(x,3)) - (3*pow(x,2)) + (8*x) -9
    return x**3 - 5*x - 9


def bissection(lower,upper):
    if abs(lower-upper)<1e-6:
        return lower
    else:
        if func(lower)*func(upper)<0:
            mid=(lower+upper)/2
            if func(lower)*func(mid)<0:
                return bissection(lower,mid)
            if func(mid)*func(upper)<0:
                return bissection(mid,upper)
            
        else:
            print("The range is not suitable")


print(bissection(2,4.5))
