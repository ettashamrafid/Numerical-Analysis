def lagrange(lst,x_interpolate):
    y_interpolate=0
    for i in range(len(lst)):
        numerator=1
        denominator=1
        for j in range(len(lst)):
            if i!=j:
                numerator= numerator*(x_interpolate - lst[j][0])
                denominator= denominator*(lst[i][0] - lst[j][0])
        temp= (numerator/denominator)* lst[i][1]
        y_interpolate+=temp
    return y_interpolate


lst=[(3,5),(6,12),(7,-10),(13,2)]
print(lagrange(lst,8))


#Using Scipy Library
from scipy.interpolate import lagrange

x=[3,6,7,13]
y=[5,12,-10,2]

f=lagrange(x,y)
print(f(8))