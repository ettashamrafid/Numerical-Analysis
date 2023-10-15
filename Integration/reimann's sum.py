import math 

def func(x):
    return pow(x,2) - 1

def reimann(lower,upper,gap):
    limit=upper -lower+1
    times= limit/gap
    left_sum=0
    right_sum=0
    for i in range(int(limit)):
        if i==0:
            left_sum+=abs(func(lower))
        elif i==times-1:
            right_sum +=abs(func(lower))
        else:
            left_sum+=abs(func(lower))
            right_sum+=abs(func(lower))
        #print(left_sum,right_sum)
        lower+=gap

    
    area= (left_sum+right_sum)/2
    return area

print(reimann(3,9,1))