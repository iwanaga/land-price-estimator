import numpy as np
np.random.seed(42)

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import TensorBoard

log_dir = './logs/simple-net'
keras.callbacks.TensorBoard(log_dir=log_dir, write_graph=True, write_grads=True, write_images=True)
