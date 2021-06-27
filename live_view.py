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
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier('frontal_face.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    img = cv2.resize(img,(224,224),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    #cv2.putText(main.main(img, 'live'))
    cv2.putText(img, main.main(img, 'live'), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    # Stop if escape key is pressed
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

    
# Release the VideoCapture object
cap.release()