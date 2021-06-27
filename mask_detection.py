import os

from tensorflow import keras
import tensorflow as tf
from keras.models import load_model
import cv2
import matplotlib.pyplot as plt
from matplotlib import image
import numpy as np
from PIL import Image
import tensorflow.python.ops.numpy_ops.np_config


def hasMask(path, type):
    model = load_model(r'mask_recog.h5')
    #input shape 244, 244, 3
    #img = image.imread(path)

    if type == 'image upload':
        cap = cv2.VideoCapture(path)
        ret, frame = cap.read()
    else:
        frame = path


    #img = np.round(np.array(img).convert('RGB').resize((224,224)),dtype=np.float32)
    #image = cv2.resize(frame, (224, 224))
    #print(img.shape)
    #img = tf.image.resize(img,(224,224))
    #img = tf.image.resize(img,(1, 224, 224))
    print(frame.shape)
    frame = cv2.resize(frame,(224,224),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    results = model.predict(frame.reshape(1,224,224,3))
    if results[0][0] > 0.7:
        return True
    else:
        return False
    #[mask, without mask]

