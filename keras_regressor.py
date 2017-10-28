import numpy as np
np.random.seed(42)
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.layers.normalization import BatchNormalization
from keras.callbacks import TensorBoard

input_filename = './input_data/filtered.csv'
log_dir = './logs/simple-net'
board = TensorBoard(log_dir=log_dir, write_graph=True, write_grads=True, write_images=True)

input_data = pd.read_csv(input_filename)
X = input_data.iloc[:, 0:4].values
Y = input_data.iloc[:, [5]].values

def regression_model():
    model = Sequential()
    model.add(Dense(4, activation='relu', input_dim=4))
    model.add(BatchNormalization())
    model.add(Dense(3, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(1))

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model


model = regression_model()
print(model.summary())
model.fit(X, Y, epochs=10000, verbose=2, validation_split=0.1, shuffle=True, callbacks=[board])
