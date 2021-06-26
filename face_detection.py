#importing Required Libraries
import cv2

face_cascade=cv2.CascadeClassifier(r'C:\Users\Paarth Bathla\Documents\Hack3\Hack3_2021\Hack3_2021\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(r'C:\Users\Paarth Bathla\Documents\Hack3\Hack3_2021\Hack3_2021\haarcascade_eye.xml')

capture=cv2.VideoCapture(0)

while True:
    ret,img=capture.read()
    grey_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(grey_image, 1.25, 4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+y,w+h),(255,255,0),2)
        rec_grey=grey_image[y:y+h,x:x+w]
        rec_color=img[y:y+h,x:x+w]


    for (ox,oy,ow,oh) in faces :
        cv2.rectangle(rec_color,(ox,oy),(ox+ow,oy+oh),(0,127,255),2)

    cv2.imshow("Face Recognition", img)
    q= cv2.waitKey(30) & 0xff
    if q==27:
        break

capture.release() 
cv2.destroyAllWindows()



