import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
import pandas as pd

# opening and reading the data and putting it in an array
data = pd.read_csv("volts-vs-time.csv", sep=",")
data = data[["v", "t", "tdiff", "log"]]
# x = time, y = volts (unused in this file), z = difference between each time lapped, w = ln(v)
x, y, z, w = data["t"], data["v"], data["tdiff"], data["log"]

std_x = x.std()
std_y = y.std()
# standard deviation of ln(v)
std_w = w.std()
# standard deviation of difference in time
std_z = z.std()
# average x and y, standard deviation for time and ln(v)
m,b = np.polyfit(x, w, 1)
print("Average Time: ", x.mean())
print("Average ln(v): ", w.mean())

# printing standard deviation
print("Standard Deviation for Time: ", std_x)
print("Standard Deviation for Voltage: ", std_y)
print("Standard Deviation for the difference in Time collected: ", std_z)
print("Standard Deviation for ln(V): ", std_w)
print("Slope:", m)

# putting time and ln(v) into graph
style.use("grayscale")
pyplot.suptitle('ln(V) vs. Time', fontsize= 20)
pyplot.scatter(x, w, color="navy")

# error bar graphs the uncertainty of each point in the y-axis for ln(v)
pyplot.errorbar(x, w, yerr=std_w, fmt='o', ecolor='navy', elinewidth=1, capsize=2)

# plots the slope
pyplot.plot(x, m*x+b, color="green")
# labels
pyplot.xlabel('Time (s)')
pyplot.ylabel('ln(V) (v)')
pyplot.show()
