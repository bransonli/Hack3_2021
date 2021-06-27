#dependencies
from tensorflow import keras
import tensorflow as tf
from keras.models import load_model
import matplotlib.pyplot as plt
from matplotlib import image
import numpy as np
from PIL import Image
import cv2

#local scripts
import mask_detection
import nose_detection
import mouth_detection

def main(path): #only takes 224, 224 dimensions
    if mask_detection.hasMask(path):
        if mouth_detection.hasMouth(path) or nose_detection.hasNose(path):
            return "mask not worn properly"
        else:
            return "mask worn properly"

    else:
        return "no mask worn"

print(main(r"C:\Users\aaron\Desktop\face_mask.jpg"))


