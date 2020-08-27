print("Loading...")

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from tkinter import filedialog, ttk, Tk

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

print("Select your file:")

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/", title = "Select file")


print("")
root.destroy()

# Disable scientific notation for clarity
np.set_printoptions(suppress=False)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5', compile=False)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open(root.filename).convert('RGB')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size)

#turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)

# Super complicated conversion and comparison process starts (from hand_Ai)
predic_to_list = prediction.tolist() 
predic2 = predic_to_list[0]

predic3 = str(predic2)

predic3 = predic3.replace("[", "")
predic3 = predic3.replace("]", "")
predic4 = predic3.replace(",", "") 
predic5 = predic4.split(" ")

result1 = float(predic5[0])
result2 = float(predic5[1])
    
if result1 < result2:
    popupmsg("This is a photo of pnuemonia")
    
elif result1 > result2:
    popupmsg("This is a photo of a normal lung")

