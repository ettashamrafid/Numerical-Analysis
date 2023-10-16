import math

def func(x):
    return pow(x,2) - 1

def simpson_3by8(lower,upper,gap=1):
    limit=int((upper-lower+1)/gap)
    if limit%2==0:
        return ("Incorrect dataset")
    else:
        sum=0
        sum += func(lower) + func(upper)
        temp=lower
        for i in range(limit-2):
            temp+=gap
            if i%3==2:
                sum += 2*func(temp)
            else:
                sum += 3*func(temp)
            
        return sum* gap * (3/8)

print(simpson_3by8(3,9))


