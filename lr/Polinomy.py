import numpy
import matplotlib.pyplot as plt

x = [98,99,100,101,103,100,95,97,92]
y = [70,75,80,85,90,87,78,73,69]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.xlabel("Temp")
plt.ylabel("BP")
plt.show()