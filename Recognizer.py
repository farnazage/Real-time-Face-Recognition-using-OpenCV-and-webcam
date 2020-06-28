import cv2
import numpy as np
from PIL import Image
import os

path='data'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");


def imgsandlables (path):
    imagePaths = [os.path.join(path,i) for i in os.listdir(path)]     
    indfaces=[]
    ids = []
    for imagePath in imagePaths:
        img = Image.open(imagePath).convert('L') # grayscale
        imgnp = np.array(img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[0])
        
        faces = detector.detectMultiScale(imgnp)
        for (x,y,w,h) in faces:
            indfaces.append(imgnp[y:y+h,x:x+w])
            ids.append(id)
    return indfaces,ids



faces,ids = imgsandlables (path)
recognizer.train(faces, np.array(ids))

id = 0
names = ['None', 'Farnaz','Alex'] 


cam= cv2.VideoCapture(0)

while True:
    _, img =cam.read()
    img = cv2.flip(img, 1) 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = detector.detectMultiScale( gray, scaleFactor = 1.3, minNeighbors = 5,)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "I dont know who this is :)"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x-5,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2) 


    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break
