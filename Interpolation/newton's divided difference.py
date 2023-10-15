import numpy as np

def newton_divided_difference(x, y, t):
    """
    Find the Newton polynomial through the points (x, y) and return its value at t.
    """

    #Newton Divided Difference Interpolation [By Bottom Science]

    # Check that the input arrays have the same length
    if len(x) != len(y):
        raise ValueError("The arrays x and y must have the same length.")

    # Initialize the polynomial
    p = [y[0]]

    # Loop over the differences
    for i in range(1, len(x)):
        # Initialize the term
        term = y[i]

        # Loop over the previous differences
        for j in range(i):
            term = (term - p[j]) / (x[i] - x[j])

        # Add the term to the polynomial
        p.append(term)

    # Evaluate the polynomial at t
    result = 0
    for i in range(len(x)):
        term = p[i]
        for j in range(i):
            term *= (t - x[j])
        result += term

    return result

# DATA POINTS (x,y)

x=[3,6,7,13]
y=[5,12,-10,2]
t = 8
p = newton_divided_difference(x, y, t)
print(p)

# Output - 0.25