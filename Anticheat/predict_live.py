import numpy as np
import pandas as pd
from keras.models import load_model
import psutil
import ctypes

# Load model
model = load_model("lstm_model.h5")
# Get process ID of Minecraft.Windows.exe
for process in psutil.process_iter(['pid', 'name']):
    if process.info['name'] == 'Minecraft.Windows.exe':
        pid = process.info['pid']
        break
else:
    print("Minecraft.Windows.exe is not running!")
    exit()
xveladdr = 0x214002DF07C-4
yveladdr = 0x214002DF07C
zveladdr = 0x214002DF07C+4
ongroundaddr = 0x214136B40D0
process_handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, pid)

while True:
    velocity_x = ctypes.c_float()
    velocity_y = ctypes.c_float()
    velocity_z = ctypes.c_float()
    onground = ctypes.c_int()
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(xveladdr), ctypes.byref(velocity_x), ctypes.sizeof(velocity_x), None)
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(yveladdr), ctypes.byref(velocity_y), ctypes.sizeof(velocity_y), None)
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(zveladdr), ctypes.byref(velocity_z), ctypes.sizeof(velocity_z), None)
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(ongroundaddr), ctypes.byref(onground), ctypes.sizeof(onground), None)
    #print(velocity_x,velocity_y,velocity_z,onground)
    # Normalize data
    data_to_predict = pd.DataFrame({
        "velocity_x": [velocity_x.value],
        "velocity_y": [velocity_y.value],
        "velocity_z": [velocity_z.value],
        "onground": [onground.value]
    })
    data_to_predict = (data_to_predict - data_to_predict.min()) / (data_to_predict.max() - data_to_predict.min())

    # Reshape input to be 3D [samples, timesteps, features]
    X = data_to_predict.values.reshape((data_to_predict.shape[0], 1, data_to_predict.shape[1]))

    # Predict labels
    predictions = model.predict(X,verbose=0)
    #if predictions >= 0.5:
        #print("Flying")
    #else:
        #print("Not flying")
    print(predictions)

