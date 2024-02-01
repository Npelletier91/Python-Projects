import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Reshape, Conv2DTranspose, BatchNormalization, LeakyReLU, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.datasets import fashion_mnist
from keras.optimizers import Adam
from keras.models import Model
from keras.layers import Input
import matplotlib.pyplot as plt
import numpy as np
import os




# Using the Fashion MNIST dataset for model testing that consists of 60,000 images and 10,000 test images
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


# Normalize the pixel values so every pixel has a value between -1 and 1
train_images = train_images / 255.0 * 2 - 1
test_images = test_images / 255.0 * 2 - 1


# Original fashion data is 2D
# Reshape the data to 4D array for the Keras convoluted layers work properly
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))





# Generator Section
def build_generator():
    model = Sequential()

    # Starting with a densely connected layer
    model.add(Dense(7 * 7 * 256, use_bias=False, input_shape=(100,)))
    model.add(BatchNormalization())
    model.add(LeakyReLU())

    # Reshape into an image of size 7x7
    model.add(Reshape((7, 7, 256)))

    # Upsample to 14x14
    model.add(Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU())

    # Upsample to 28x28
    model.add(Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU())

    # Final output layer with tanh activation
    model.add(Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))

    return model

generator = build_generator()





# Discriminator Section
def build_discriminator(image_shape):
    model = Sequential()
    
    model.add(Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=image_shape))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dropout(0.3))

    model.add(Conv2D(128, (5, 5), strides=(2, 2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dropout(0.3))

    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    
    return model


image_shape = (28, 28, 1)
discriminator = build_discriminator(image_shape)
discriminator.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5), metrics=['accuracy'])





def build_gan(generator, discriminator):
    # Make the discriminator not trainable when combined with the generator
    discriminator.trainable = False

    # Input for the generator. Noise of random value tensor of 100 by 1
    z = Input(shape=(100,))
    # Calls the generator with the noise and outputs an image
    img = generator(z)

    # Discriminator takes generated images as input and determines validity
    validity = discriminator(img)

    # The combined model (stacked generator and discriminator)
    combined = Model(z, validity)
    combined.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5))

    return combined

gan = build_gan(generator, discriminator)




# Saving images to evaluate model as it progresses in epochs
def save_imgs(epoch):
    output_dir = "images"  # Define the directory for output images
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it does not exist

    r, c = 5, 5  # Grid size
    noise = np.random.normal(0, 1, (r * c, noise_dim))
    gen_imgs = generator.predict(noise)

    # Rescale images from [-1, 1] to [0, 1]
    gen_imgs = 0.5 * gen_imgs + 0.5

    fig, axs = plt.subplots(r, c)
    cnt = 0
    for i in range(r):
        for j in range(c):
            axs[i,j].imshow(gen_imgs[cnt, :, :, 0], cmap='gray')
            axs[i,j].axis('off')
            cnt += 1
    fig.savefig(f"{output_dir}/{epoch}.png")  # Save the figure
    plt.close()
    print(f"Image for epoch {epoch} saved in {output_dir}/") 





# Hyperparameters
batch_size = 128
epochs = 2000
noise_dim = 100  # Dimensionality of the noise vector


# Create a batch of real labels (1s) and fake labels (0s)
real_labels = np.ones((batch_size, 1))
fake_labels = np.zeros((batch_size, 1))


for epoch in range(epochs):
    
    # 1. Train the Discriminator #
    
    
    # Select a random batch of 128 real images out of 60,000
    idx = np.random.randint(0, train_images.shape[0], batch_size)
    real_imgs = train_images[idx]
    
    # Generate a batch of fake images
    noise = np.random.normal(0, 1, (batch_size, noise_dim))
    fake_imgs = generator.predict(noise)
    
    # Train the Discriminator
    d_loss_real = discriminator.train_on_batch(real_imgs, real_labels)
    d_loss_fake = discriminator.train_on_batch(fake_imgs, fake_labels)
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
    
    
    # 2. Train the Generator #
    
    
    # Generate a new batch of noise
    noise = np.random.normal(0, 1, (batch_size, noise_dim))
    
    # Train the generator (to have the discriminator label samples as real)
    g_loss = gan.train_on_batch(noise, real_labels)
    
    # Print the progress every 50 epochs
    if epoch % 50 == 0:
        print(f"{epoch} [D loss: {d_loss[0]}, acc.: {100*d_loss[1]}%] [G loss: {g_loss}]")
        
    # Save images at every 100 epochs and the last epoch
    if epoch % 100 == 0 or epoch == 1999:
        save_imgs(epoch)


# Save the GAN for later use of generating an image
generator.save('generator_model.h5')
