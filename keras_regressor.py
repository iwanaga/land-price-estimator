import numpy as np
np.random.seed(42)
import pandas as pd

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import TensorBoard

input_filename = './input_data/filtered.csv'
log_dir = './logs/simple-net'
keras.callbacks.TensorBoard(log_dir=log_dir, write_graph=True, write_grads=True, write_images=True)

input_data = pd.read_csv(input_filename)
X = input_data.iloc[:, 0:4]
Y = input_data.iloc[:, [5]]
