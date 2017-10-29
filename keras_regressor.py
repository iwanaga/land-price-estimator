import numpy as np
np.random.seed(42)
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.layers.normalization import BatchNormalization
from keras.callbacks import TensorBoard

input_filename = './input_data/filtered.csv'
target_filename = './input_data/target.csv'
log_dir = './logs/simple-net'
board = TensorBoard(log_dir=log_dir, write_graph=True, write_grads=True, write_images=True)

# input data を 0 から 1 の値に normalize し、説明変数と目的変数に分離する。
input_data = pd.read_csv(input_filename)
normalized_input = (input_data - input_data.min()) / (input_data.max() - input_data.min())
X = normalized_input.iloc[:, 0:5].values
Y = normalized_input.iloc[:, [5]].values

# 予測対象を同様に normalize
target_data = pd.read_csv(target_filename)
explanatories = input_data.iloc[1:, 0:5]
normalized_target = ((target_data - explanatories.min()) / (explanatories.max() - explanatories.min())).values


def regression_model():
    model = Sequential()
    model.add(Dense(5, activation='relu', input_dim=5))
    model.add(BatchNormalization())
    model.add(Dense(3, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(1))

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model


model = regression_model()
print(model.summary())
model.fit(X, Y, epochs=2500, verbose=2, validation_split=0.1, shuffle=True, callbacks=[board])


def denormalize(normalized_price):
    min_price = input_data.min()[5]
    max_price = input_data.max()[5]
    return (max_price - min_price) * normalized_price + min_price


# 予測
results = model.predict(normalized_target)
print(results)

# normalize された予測値を円に戻す
estimated_prices = [
    denormalize(results[0][0]),
    denormalize(results[1][0]),
    denormalize(results[2][0])
]
print(estimated_prices)
