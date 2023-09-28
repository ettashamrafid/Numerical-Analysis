import math
def func(x):
    return (-pow(x,2)+(9*x)-20)
    #return (4*pow(x,3)) - (3*pow(x,2)) + (8*x) -9
    return x**3 - 5*x - 9

def false_position(lower,upper,r=[0]):
    if func(lower)*func(upper)<0:
        next= ((lower*func(upper))-(upper*func(lower)))/(func(upper)-func(lower))
        r.append(next)
        if abs(r[-1]-r[-2])>1e-6:
            if func(next)<0:
                return false_position(next,upper)
            else:
                return false_position(lower,next)
        else:
            return next
        
    else:
        print("The range is not correct")

print(false_position(3,4.5))