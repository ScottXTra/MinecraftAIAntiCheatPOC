import argparse
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

parser = argparse.ArgumentParser()
parser.add_argument('data_file', help='path to the training data file')
args = parser.parse_args()

data = pd.read_csv(args.data_file)

X = data.iloc[:, :6].values
y = data.iloc[:, 6].values

X = np.reshape(X, (X.shape[0], 1, X.shape[1]))

model = Sequential()
model.add(LSTM(64, input_shape=(1, 6)))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, batch_size=64, epochs=20, validation_split=0.2)

model.save('flying_detection_model.h5')
