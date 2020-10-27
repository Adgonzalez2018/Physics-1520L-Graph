import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
import pandas as pd
import math

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
print("Average Time: ", x.mean())
print("Average Voltage: ", y.mean())
print("Standard Deviation for Time: ", std_x)
print("Standard Deviation for Voltage: ", std_y)
print("Standard Deviation for the difference in Time collected: ", std_z)
print("Standard Deviation for ln(V): ", std_w)
# putting it into the matplotlib
style.use("ggplot")
pyplot.suptitle('ln(v) vs. Time', fontsize= 20)
pyplot.scatter(x, w, color="navy")
# error bar graphs the uncertainty of each point in accordance to time
pyplot.errorbar(x, w, xerr=std_z, fmt='o', ecolor='navy', elinewidth=1, capsize=2)
m,b = np.polyfit(x, w, 1)
pyplot.plot(x, m*x+b, color="black")
pyplot.xlabel('Time (s)')
pyplot.ylabel('ln(v) (v)')
pyplot.show()
