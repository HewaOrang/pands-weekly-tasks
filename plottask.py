# plottask.py
# This program plotts a hist of a normal dist of 1000 values with a mean of 5 and std of 2
# and a plot of the function h(x)=x^3 in the range 0 to 10 on the one axis
# Author: Hewa Orang
# Reference: https://www.w3schools.com/python/python_ml_normal_data_distribution.asp

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

'''
np.random.seed(1) 
normal_dist = np.random.normal(5.0, 2.0, 1000)

plt.hist(normal_dist)
plt.show()

'''

x = np.linspace(0.0, 10.0, 400)
h = x**3

ax.plot(x, h, label= 'h(x) = x³')
ax.set_title('function h(x)=x³')
ax.set_xlabel('x')
ax.set_ylabel('h(x)')
ax.legend()

plt.savefig('WT8_functionplot')

