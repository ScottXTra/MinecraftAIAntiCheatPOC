import argparse
import pandas as pd
import numpy as np
from keras.models import load_model
parser = argparse.ArgumentParser()
parser.add_argument('model_file', help='path to the saved model file')
parser.add_argument('data_file', help='path to the data file to predict')
args = parser.parse_args()
model = load_model(args.model_file)
data = pd.read_csv(args.data_file)
X = data.iloc[:, :6].values
X = np.reshape(X, (X.shape[0], 1, X.shape[1]))
y_pred = model.predict(X)
avg_pred = np.mean(y_pred)
if avg_pred > 0.5:
    print("Flying" + " -> " + str(avg_pred))
else:
    print("Not flying"+ " -> " + str(avg_pred))
