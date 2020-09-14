import numpy as np
import tensorflow as tf
from tensorflow import keras

data = np.random.rand(250, 5)
labels = (np.sum(data, axis=1) > 2.5) * 1
labels = np_utils.to_categorical(labels)

print(labels)