import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM

# Load and preprocess data
print("Loading data...")
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
df = pd.read_csv(url, usecols=[1])
print("Data loaded.")

# Scaling data
print("Scaling data...")
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df.values)
print("Data scaled.")

# Convert time series to supervised learning problem
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # Input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
    # Forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
    agg = pd.concat(cols, axis=1)
    if dropnan:
        agg.dropna(inplace=True)
    return agg

# Frame as supervised learning
n_hours = 3  # Number of lag hours
reframed = series_to_supervised(scaled_data, n_hours, 1)
reframed = reframed[n_hours:]

# Total number of samples in the original dataset
total_samples = df.shape[0]

# Number of samples to use for training (all samples up to the last 12 months, adjusted for lags)
n_train_samples = total_samples - 12 - n_hours

# Split into train and test sets
values = reframed.values
train = values[:n_train_samples, :]
test = values[n_train_samples:, :]
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]

# Reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], n_hours, 1))
test_X = test_X.reshape((test_X.shape[0], n_hours, 1))

# Check if any array is empty
if train_X.size == 0 or train_y.size == 0:
    raise ValueError("Training data is empty. Check the data preprocessing and splitting steps.")

print(f"train_X shape: {train_X.shape}")
print(f"train_y shape: {train_y.shape}")

# Build the LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Diagnostic prints
print(f"train_X shape: {train_X.shape} - Number of training samples: {train_X.shape[0]}")
print(f"train_y shape: {train_y.shape}")
print(f"test_X shape: {test_X.shape} - Number of testing samples: {test_X.shape[0]}")
print(f"test_y shape: {test_y.shape}")
# Train the model
model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)

# Forecasting for 1961
yhat = model.predict(test_X)

# Inverse transform the predictions
inv_yhat = scaler.inverse_transform(yhat)

# Inverse transform the actual values
test_y_reshaped = test_y.reshape(-1, 1)
inv_y = scaler.inverse_transform(test_y_reshaped)

# Print predicted values
print("Predicted Passenger Values:")
for i in range(len(inv_yhat)):
    print(f"Month {i+1}: Predicted: {inv_yhat[i][0]:.0f}, Actual: {inv_y[i][0]:.0f}")


# Calculate RMSE
from sklearn.metrics import mean_squared_error
from math import sqrt
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)
