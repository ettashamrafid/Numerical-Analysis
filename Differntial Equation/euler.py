import matplotlib.pyplot as plt

def differential_eqn(x,y):
    return y-x

def euler(x_i=0,y_i=0,h=0.1):
    x,y=x_i,y_i
    lst=[(x,y)]
    for i in range(1000):
        derivative= differential_eqn(x,y)
        x=x+h
        y=y+(derivative*h)
        lst.append((x,y))
    return lst




xs, ys = zip(*euler(0,2))
plt.plot(xs, ys)
plt.show()