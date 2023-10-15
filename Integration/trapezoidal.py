import math 

def func(x):
    return pow(x,2) - 1

def trapezoid(lower,upper,gap=1):
    temp=lower
    limit=int((upper-lower)/gap)
    sum=0
    for i in range(limit):
        temp_sum= func(temp)+ func(temp+gap)
        area= 0.5*temp_sum*gap
        sum+=abs(area)
        temp+=gap
    
    return sum


print(trapezoid(3,9))