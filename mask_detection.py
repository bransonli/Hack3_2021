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


    image = image.imread(path) 
    #image = cv2.resize(frame, (224, 224))
    print(image.shape)
    results = model.predict(image.reshape((1,224,224,3)))
    return results
    #[mask, without mask]

