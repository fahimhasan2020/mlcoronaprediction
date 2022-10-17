#Three lines to make our compiler able to draw:
import sys
import matplotlib
from tkinter import *
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from scipy import stats

x = [94,90,88,87,80,78,70,68,62]
y = [2,4,6,8,10,12,14,16,18]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.title('Time vs Board temperature efficiency Linear graph')
plt.xlabel('Time in month')
plt.ylabel('Oxygen saturation')
plt.plot(x, mymodel)
plt.show()

# #Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
# import matplotlib.pyplot as plt

# x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# plt.scatter(x, y, c=classes)
# plt.xlabel('Time')
# plt.ylabel('Oxygen saturation')
# plt.show()
