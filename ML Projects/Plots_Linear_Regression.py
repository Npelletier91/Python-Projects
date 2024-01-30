import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import SGDRegressor


df = pd.read_csv('dataset_1.csv')

print(df.head())

df = df[['column_1','column_2']]

#df.plot(kind='scatter', x='column_1', y='column_2')
#plt.figure(figsize=(12,8))
#plt.title('Example')
#plt.show()

X = df[['column_1']].values
y = df[['column_2']].values

model = SGDRegressor()
model.fit(X,y)

print("Coefficient (Slope):", model.coef_[0])
print("Intercept:", model.intercept_)


y_pred = model.predict(X)


plt.scatter(X,y, color='blue')
plt.plot(X, y_pred, color='red')
plt.show()
