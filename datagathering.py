#data gathering for each individul

import cv2
import os

os.chdir("CurrentPath")

Detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam= cv2.VideoCapture(0)

id = input('\n enter user id end press Enter: ')
count = 0
while(True):
    _, img= cam.read()
    img= cv2.flip(img, 1) # Flip camera vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detection.detectMultiScale(gray,1.3,5 )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        count += 1

        cv2.imwrite("datagathering/" + str(id) + '.' +  str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)

    k = cv2.waitKey(100) &  0xFF == ord('s'):
    if k == 10:
        break
    elif count >= 30: 
         break
