import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv('ML Projects\exampledataset2.csv')

X_train = df['text']

y_train = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

vectorized_data = CountVectorizer()
X_train_vectorized = vectorized_data.fit_transform(X_train)
X_test_vectorzied = vectorized_data.transform(X_test)

model = SVC()
model.fit(X_train_vectorized, y_train)

prediction = model.predict(X_test_vectorzied)

accuracy = accuracy_score(prediction, y_test)

print(accuracy)