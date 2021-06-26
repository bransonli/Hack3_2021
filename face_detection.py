#importing Required Libraries
import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier(r'C:\Users\Paarth Bathla\Documents\Hack3\Hack3_2021\Hack3_2021\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(r'C:\Users\Paarth Bathla\Documents\Hack3\Hack3_2021\Hack3_2021\haarcascade_eye.xml')

capture=cv2.VideoCapture(0)

while True:
    img_counter=0
    ret,img=capture.read()
    grey_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(grey_image, 1.25, 4)

    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+y,w+h),(255,255,0),2)
        rec_grey=grey_image[y:y+h,x:x+w]
        rec_color=img[y:y+h,x:x+w]


    for (ox,oy,ow,oh) in faces :
        cv2.rectangle(rec_color,(ox,oy),(ox+ow,oy+oh),(0,127,200),2)

    try:
        check, frame = capture.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            capture.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 200x150 scale...")
            img_ = cv2.resize(gray,(50,50))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
        
            break
        elif key == ord('q'):
            print("Turning off camera.")
            capture.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        capture.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
    


capture.release() 
cv2.destroyAllWindows()





