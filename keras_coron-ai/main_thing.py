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

model_selection = os.getenv('model_select')

if model_selection == None:
    input0 = input("Would you like to use .(H)5 or (S)avedModel")
    if input0 == "H":
        os.environ['model_select'] = 'H'
        global model
        model = keras.models.load_model('xrayble_2.h5')
    elif input0 == "S":
        os.environ['model_select'] = 'S'
        model = keras.models.load_model('xrayble_2')
elif model_selection == "H":
    model = keras.models.load_model('xrayble_2.h5')
elif model_selection == "S":
    model = keras.models.load_model('xrayble_2')


if input0 == "H":
    model = keras.models.load_model('xrayble_2.h5')
elif input0 == "S":
    model = keras.models.load_model('xrayble_2')

img_height = 180
img_width = 180

NORM_FONT = ("Verdana", 11)

def pick_file():
    root2 = Tk()
    root2.withdraw()
    root2.filename = askopenfilename()

    global filename
    filename = root2.filename
  
def popupmsg(msg):
    popup = Tk()
    popup.wm_title("Result")
    
    label = ttk.Label(popup, text=msg, font=NORM_FONT)

    label.pack(anchor='center')
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def popupmsg2(msg):
    popup = Tk()
    popup.wm_title("Analyze?")
    
    label = ttk.Label(popup, text=msg, font=NORM_FONT)

    label.pack(anchor='center')
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

pick_file()

messagebox.showinfo("Analyze?", "Analyze? It will take about 30 seconds")
print("")

img = keras.preprocessing.image.load_img(
    filename, target_size=(img_height, img_width)
)

img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

wow = [class_names[np.argmax(score)], 100 * np.max(score)]

yay = "This is " + wow[0] + ": " + str(wow[1])
popupmsg(yay)
