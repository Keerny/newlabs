import math
import matplotlib.pyplot as plt
import numpy as np
from one import *

fig, ax = plt.subplots()
x = rect_integral(fn,0,math.pi/4,10000)
y = tr_integral(fn,0,math.pi/4,10000)
z = simpsons_(lower_limit, upper_limit, n)
ax.scatter(1, x)
ax.scatter(2, y)
ax.scatter(3, z)

plt.show()