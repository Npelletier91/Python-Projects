import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.utils import to_categorical
from keras.datasets import fashion_mnist


# Using the Fashion MNIST dataset for model testing 
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


# Normalize the pixel values so every pixel has a value between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# Original fashion data is 2D
# Reshape the data to 4D array for the Keras convoluted layers work properly
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))


# Labeling data to binary class matrices (one-hot encoding)
y_train = to_categorical(train_labels, 10)
y_test = to_categorical(test_labels, 10)


model = Sequential()


model.add(Conv2D(28, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(56, (3, 3), activation='relu'))
model.add(Dropout(rate=0.15))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(56, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(112, activation='relu'))
model.add(Dense(10, activation='softmax'))


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


model.fit(train_images, y_train, epochs=10, batch_size=64)


loss, accuracy = model.evaluate(test_images, y_test)
print(f"Test accuracy: {accuracy}")
