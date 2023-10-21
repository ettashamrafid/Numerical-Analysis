import matplotlib.pyplot as plt

def differential_eqn(x,y):
    return y-x


def rungey_kutta(x_i,y_i,h=0.1):
    lst=[(x_i,y_i)]
    for i in range(1000):
        k1= h*differential_eqn(x_i,y_i)
        k2= h*differential_eqn(x_i+ 0.5*h, y_i + k1*0.5)
        k3= h*differential_eqn(x_i+ 0.5*h, y_i + k2*0.5)
        k4= h*differential_eqn(x_i+ 0.5*h, y_i + k3*0.5)
        k= (k1+ (2*k2) + (2*k3) + k4) * (1/6)

        x_i= x_i + h
        y_i= y_i + k
        lst.append((x_i,y_i))
    
    return lst

xs,ys= zip(*rungey_kutta(0,2))
plt.plot(xs,ys)
plt.show()
