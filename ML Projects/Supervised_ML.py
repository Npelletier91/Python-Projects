import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('ML Projects\exampledataset1.csv')

X = df.drop("Target", axis=1)
Y = df["Target"]


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(f"X_test", X_test.count())
print(f"X_train", X_train.count())
print(f"Y_test", Y_test)
print(f"Y_train", Y_train.count())

model = LogisticRegression()
trained_model = model.fit(X_train, Y_train)
print(f"Trained model: ", trained_model)

prediction = model.predict(X_test)
print(f"Predictions: ", prediction)


accuracy = accuracy_score(prediction, Y_test)
print(f"Accuracy: ", accuracy)