import sys
import matplotlib
from tkinter import *
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy import stats

mangoColor = [85,85,87,90,92,65,64,67,68,72,56,43,48,49,50]
ratioOfGlucose = [96,95,97,93,45,88,85,82,93,41,37,35,38,39,85]


slope, intercept, r, p, std_err = stats.linregress(mangoColor, ratioOfGlucose)

def myfunc(mangoColor):
  return slope * mangoColor + intercept

mymodel = list(map(myfunc, mangoColor))

plt.scatter(mangoColor, ratioOfGlucose)
plt.plot(mangoColor, mymodel)
plt.xlabel("Beta carotine in parcentese")
plt.ylabel("Parcentese of Glucose")
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
