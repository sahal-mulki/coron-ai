import tensorflow.keras
from PIL import ImageOps
import numpy as np
from tkinter import filedialog, ttk, Tk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

NORM_FONT = ("Verdana", 11)

def pick_file():
    root2 = Tk()
    root2.withdraw()
    root2.filename = askopenfilename()

    global filename
    filename = root2.filename
  
def popupmsg(image, msg):
    popup = Tk()
    popup.wm_title("Result")

    img = Image.open(image)
    image = ImageOps.fit(img, (300, 300))
    
    photo = ImageTk.PhotoImage(image)
    lab = ttk.Label(image=photo)
    lab.pack()
    
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
# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5', compile=False)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open(filename).convert('RGB')

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

result1 = result1 * 100
result2 = result2 * 100

if result2 == 100:
    result1 = 0

if result1 == 100:
    result2 = 0
    
if result1 < result2:
    popupmsg(filename, "This is Pneumonia : " + str(result2) + "%")
    
elif result1 > result2:
    popupmsg(filename, "This is Normal : " + str(result1) + "%")

