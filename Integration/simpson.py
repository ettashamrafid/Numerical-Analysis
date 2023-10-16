import math

def func(x):
    return pow(x,2) - 1


def simpson(lower,upper,gap=1):
    input_no= int((upper-lower+1)/gap)
    if input_no%2==0:
        return ("Incorrect DataSet")
    else:
        sum=0
        sum+= func(lower) +func(upper)
        for i in range(lower+gap,upper,2):
            temp= 4*func(i)
            sum+=temp
        for i in range(lower+(2*gap), upper, 2):
            temp= 2*func(i)
            sum+=temp

        return sum *(gap/3)
    

print(simpson(2,8))

