from scipy import stats

x = [1,2,3,4,5,6,7,8,9]
y = [96,95,94,94,93,92,95,90,88]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(8)

print(speed)