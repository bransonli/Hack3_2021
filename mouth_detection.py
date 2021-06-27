import cv2
import numpy as np


def hasMouth(path, type):
  mouth_cascade = cv2.CascadeClassifier(r'mouth.xml')

  if mouth_cascade.empty():
    raise IOError('Unable to load the nose cascade classifier xml file')

  if type == 'image upload':
    cap = cv2.VideoCapture(path)
    ret, frame = cap.read()
  else:
    frame = path

  ds_factor = 0.5

  frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  mouth_rects = mouth_cascade.detectMultiScale(gray, 1.3, 5)

  if mouth_rects == ():
    return False
  else:
    return True









