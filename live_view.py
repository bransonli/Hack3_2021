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
import main

# Load the cascade
face_cascade = cv2.CascadeClassifier('frontal_face.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(2)
cap.set(3, 400)
cap.set(4, 400)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    img = tf.image.resize(img, (224, 224))
    cv2.putText(main.main(img, 'live'))
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()