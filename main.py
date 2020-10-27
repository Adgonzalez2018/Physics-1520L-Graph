import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
import pandas as pd

# opening and reading the data and putting it in an array
data = pd.read_csv("volts-vs-time.csv", sep=",")
data = data[["v", "t", "tdiff"]]
y, x, z = data["t"], data["v"], data["tdiff"]
std_x = x.std()
std_y = y.std()

# standard deviation of difference in time
std_z = z.std()
# average x and y, standard deviation for time and volts
print("Average Voltage: ", x.mean())
print("Average Time: ", y.mean())
print("Standard Deviation for Voltage: ", x.std())
print("Standard Deviation for Time: ", y.std())
print("Standard Deviation for the difference in Time collected: ", z.std())
# putting it into the matplotlib
style.use("ggplot")
pyplot.suptitle('Time vs Voltage', fontsize= 20)
pyplot.scatter(x, y, color="navy")
# error bar graphs the uncertainty of each point in accordance to time
pyplot.errorbar(x, y, yerr=std_z, fmt='o', ecolor='navy', elinewidth=1, capsize=2)
m,b = np.polyfit(x, y, 1)
pyplot.plot(x, m*x+b, color="black")
pyplot.xlabel('Time (s)')
pyplot.ylabel('Voltage (v)')
pyplot.show()
