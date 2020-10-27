import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
import pandas as pd

# opening and reading the data and putting it in an array
data = pd.read_csv("volts-vs-time.csv", sep=",")
data = data[["v", "t", "tdiff"]]

# x = time, y = volts, z = difference between each time lapped,
y, x, z = data["t"], data["v"], data["tdiff"]
# standard deviation of time
std_x = x.std()
# standard deviation of voltage
std_y = y.std()
# standard deviation of difference in time (which is used in the graph)
std_z = z.std()

# prints average x and y, standard deviation for time and volts and time difference
print("Average Voltage: ", x.mean())
print("Average Time: ", y.mean())
print("Standard Deviation for Voltage: ", x.std())
print("Standard Deviation for Time: ", y.std())
print("Standard Deviation for the difference in Time collected: ", z.std())

# putting time and voltage into graph
style.use("grayscale")
pyplot.suptitle('Time vs Voltage', fontsize= 20)
pyplot.scatter(x, y, color="navy")

# error bar graphs the uncertainty of the difference in time
pyplot.errorbar(x, y, yerr=std_z, fmt='o', ecolor='navy', elinewidth=1, capsize=2)
# labels
pyplot.xlabel('Voltage (v)')
pyplot.ylabel('Time (s)')
pyplot.show()
