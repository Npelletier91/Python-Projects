import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv('ML Projects\exampledataset2.csv')

X_train = df['text']

y_train = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

print(f'Text data count: ', X_train.count())
print(f'Test Text data count: ', X_test.count())


vectorized_data = CountVectorizer()
X_train_vectorized = vectorized_data.fit_transform(X_train)
X_test_vectorzied = vectorized_data.transform(X_test)

# Get feature names (words) from the vocabulary
feature_names = vectorized_data.get_feature_names_out()


# Print labeled data alongside the sparse matrix
for i, (data, label) in enumerate(zip(X_train, y_train)):
    print(f"Row {i} - Label: {label}, Text: {data}")

    # Print the corresponding sparse matrix row with words
    print([(feature_names[j], X_train_vectorized[i, j]) for j in range(X_train_vectorized.shape[1]) if X_train_vectorized[i, j] != 0])
    print("\n" + "="*50 + "\n")


model = SVC()
model.fit(X_train_vectorized, y_train)

prediction = model.predict(X_test_vectorzied)

accuracy = accuracy_score(prediction, y_test)

print(accuracy)