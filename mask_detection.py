import os

from tensorflow import keras
import tensorflow as tf
from keras.models import load_model
import cv2
import matplotlib.pyplot as plt
from matplotlib import image
import numpy as np
from PIL import Image

model = load_model(r'C:\Users\aaron\Desktop\Hack3_2021\mask_recog.h5')
#input shape 244, 244, 3


image = image.imread(r'C:\Users\aaron\Desktop\face_mask_adobe.jpg') 
#image = cv2.resize(frame, (224, 224))
print(image.shape)
a = model.predict(image.reshape((1,224,224,3)))
print(a)
#[mask, without mask]

