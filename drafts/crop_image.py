import cv2 
import numpy as np

img1=cv2.imread(r'C:\Users\Paarth Bathla\Documents\Hack3\Hack3_2021\Hack3_2021\saved_img.jpg')
cv2.imshow("original", img1)

cropped_image= img1[200:550, 300:500]
cv2.imshow("cropped", cropped_image)
cv2.imwrite("Cropped Image.jpg", cropped_image)
    