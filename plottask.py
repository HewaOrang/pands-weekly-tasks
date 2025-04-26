# plottask.py
# This program plotts a hist of a normal dist of 1000 values with a mean of 5 and std of 2
# and a plot of the function h(x)=x^3 in the range 0 to 10 on the one axis
# Author: Hewa Orang
# Reference: https://www.w3schools.com/python/python_ml_normal_data_distribution.asp

# Imports libraries
import numpy as np 
import matplotlib.pyplot as plt

# Create figure and axis
fig, ax = plt.subplots()

# Generate normal distribution data.
np.random.seed(1)   # set seed to produce the same random number set every time the program is ran.
normal_dist = np.random.normal(5.0, 2.0, 1000)  # Mean=5, Std=2, 1000 samples

# Plot histogram on the same axes.
ax.hist(normal_dist, bins=30, alpha=0.6, label= 'Normal Distribution (mean=5, std=2)')

# Generate x values for h(x) = x³
x = np.linspace(0.0, 10.0, 400)
h = x**3

# Plot the function on the same axes
ax.plot(x, h, color= 'red', label= 'h(x) = x³')

# Set title and labels
ax.set_title('Histogram & function h(x)=x³')
ax.set_xlabel('x')
ax.set_ylabel('h(x)')

# Show legend
ax.legend()

# Saves and shows the figure
plt.savefig('WT8_functionplot')
plt.show()
