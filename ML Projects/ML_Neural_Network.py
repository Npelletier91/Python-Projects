import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, BatchNormalization, Activation
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split

df = mnist.load_data()

(X_train, y_train), (X_test, y_test) = df


X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=123)

model = Sequential()
model.add(Flatten(input_shape=(28, 28)))  # Flatten the 28x28 images

model.add(Dense(10))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Dense(10))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Dense(10, activation="softmax"))

model.compile(optimizer=Adam(learning_rate=0.01), loss="sparse_categorical_crossentropy", metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val), batch_size=32)

loss, accuracy = model.evaluate(X_test, y_test)

print(loss)
print(accuracy)