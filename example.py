from polyFormConversion import getNumpy1D
import numpy as np

x = getNumpy1D("12x^3-11x^2+9x+18")
y = getNumpy1D("4x+3")

quotient, remainder = np.polydiv(x, y)
print(quotient)
print(remainder)
