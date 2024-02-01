from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

# Load the model
generator = load_model('generator_model.h5')

# Generate images
def generate_image(generator, noise_dim=100):
    noise = np.random.normal(0, 1, (1, noise_dim))
    generated_image = generator.predict(noise)
    generated_image = 0.5 * generated_image + 0.5  # Rescale images from [-1, 1] to [0, 1]

    plt.imshow(generated_image[0, :, :, 0], cmap='gray')
    plt.axis('off')
    plt.show()

# Call the function to generate a new image
generate_image(generator)