import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
import pandas as pd

# opening and reading the data and putting it in an array
data = pd.read_csv("volts-vs-time.csv", sep=",")
data = data[["v", "t", "tdiff", "log"]]
x, y, z, w = data["t"], data["v"], data["tdiff"], data["log"]
std_x = x.std()
std_y = y.std()
std_w = w.std()

# standard deviation of difference in time
std_z = z.std()
# average x and y, standard deviation for time and volts
m,b = np.polyfit(x, w, 1)
print("Average Time: ", x.mean())
print("Average ln(v): ", w.mean())
print("Standard Deviation for Time: ", std_x)
print("Standard Deviation for Voltage: ", std_y)
print("Standard Deviation for the difference in Time collected: ", std_z)
print("Standard Deviation for ln(V): ", std_w)
print("Slope:", m)
# putting it into the matplotlib
style.use("grayscale")
pyplot.suptitle('ln(V) vs. Time', fontsize= 20)
pyplot.scatter(x, w, color="navy")
# error bar graphs the uncertainty of each point in accordance to time
pyplot.errorbar(x, w, yerr=std_w, fmt='o', ecolor='navy', elinewidth=1, capsize=2)

pyplot.plot(x, m*x+b, color="green")
pyplot.xlabel('Time (s)')
pyplot.ylabel('ln(V) (v)')
pyplot.show()
