import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('dataset_2.csv')

X = df.drop('species', axis=1)
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

model = LogisticRegression()
model.fit(X_train, y_train)

preditcion = model.predict(X_test)
accuracy = (preditcion == y_test).sum().item()/len(y_test)

print(preditcion)
print(accuracy)