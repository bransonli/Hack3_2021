import os

from tensorflow import keras
import tensorflow as tf
from keras.models import load_model
import cv2
import matplotlib.pyplot as plt
from matplotlib import image
import numpy as np
from PIL import Image


def hasMask(path):
    model = load_model(r'mask_recog.h5')
    #input shape 244, 244, 3
    #img = image.imread(path)

    capture = cv2.VideoCapture(path) 
    ret,img= capture.read()
    #img = np.round(np.array(img).convert('RGB').resize((224,224)),dtype=np.float32)
    #image = cv2.resize(frame, (224, 224))
    #print(img.shape)
    #img = tf.image.resize(img,(224,224))
    #img = tf.image.resize(img,(1, 224, 224))
    results = model.predict(img.reshape(1,224,224,3))
    if results[0][0] > results[0][1]:
        return True
    else:
        return False
    #[mask, without mask]

