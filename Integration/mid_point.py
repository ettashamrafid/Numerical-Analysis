import math

def func(x):
    return pow(x,2) - 1


def mid_point(lower,upper,gap=1):
    limit=int((upper-lower)/gap)
    temp=lower
    area=0
    for i in range(limit):
        temp_x=(temp+temp+gap)/2
        area+= (func(temp_x)*gap)

        temp+=gap
    return area


print(mid_point(2,8))