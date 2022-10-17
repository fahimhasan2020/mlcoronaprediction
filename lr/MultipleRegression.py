import pandas 
from sklearn import linear_model
df = pandas.read_excel("data.xlsx",engine='openpyxl')
X = df[['bt', 'temp','wt']]
y = df['gas']
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedTaste = regr.predict([[48, 27, 23]])
print(predictedTaste)