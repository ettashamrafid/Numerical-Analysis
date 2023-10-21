import matplotlib.pyplot as plt

def differential_eqn(x,y):
    return y-x

def euler(x_i=0,y_i=0,h=0.1):
    x,y=x_i,y_i
    lst=[(x,y)]
    for i in range(1000):
        initial_x=x
        initial_y=y
        derivative=differential_eqn(initial_x,initial_y)
        y_n=initial_y +(derivative*h)
        x_n=initial_x+h
        for i in range(3):
            temp= differential_eqn(initial_x,initial_y)+ differential_eqn(x_n,y_n)
            y_next= initial_y + temp*h*0.5
            y_n=y_next
        
        lst.append((x_n,y_n))
        x=x_n
        y=y_n


    return lst




xs, ys = zip(*euler(0,2))
plt.plot(xs, ys)
plt.show()