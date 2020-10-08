from PIL import ImageOps
from tkinter import filedialog, ttk, Tk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import os, PIL, tensorflow.keras
import PIL
import tensorflow as tf
import numpy as np

class_names = ["Normal", "Pnuemonia"]

model = keras.models.load_model('xrayble')

img_path = input("Enter the path of your image")
try:
    img = keras.preprocessing.image.load_img(
        img_path, target_size=(180, 180)
    )
except:
    print('Path not found')
    exit(0)

img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

wow = [class_names[np.argmax(score)], 100 * np.max(score)]

yay = "This is " + wow[0] + ": " + str(wow[1])
print(yay)
