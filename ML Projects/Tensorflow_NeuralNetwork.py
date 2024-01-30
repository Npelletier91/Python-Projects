import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense

data = pd.read_csv('dataset_2.csv')

X = data.drop(columns='species')
y = data['species']
le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

model = Sequential()
model.add(Dense(10, activation= 'relu'))
model.add(Dense(10, activation= 'relu'))
model.add(Dense(len(y), activation='softmax'))

model.compile(optimizer='adam', loss= 'sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=10, epochs=20)

_, accuracy = model.evaluate(X_test, y_test)

print(accuracy)
