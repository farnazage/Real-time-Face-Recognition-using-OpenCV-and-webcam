# Real-time-Face-Recognition-using-OpenCV-and-webcam


I used the OpenCV library in Python to do a real-time Face recognition using the computer webcam.
https://opencv.org/

Face detection is done using feature-based cascade classifiers.
https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html

This project contains 2 python scripts. The  first script is the datagathering in which individuals' pictures are gathered to be uses in the recognition process.
the recognizer script with then train and run the model.

Before starting the data gathering, a driectory for the project should be created.
mkdir project

haarcascade_frontalface_default.xml should be downloaded to the project's directory.

(the project directory should containg the python scripts and the haarcascade part.)

then the "subdirectory" for datagathering should be created. In this subdirectory picture samples for each individual is stored.

mkdir data


haarcascade_frontalface_default.xml:
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

Based on a complete Tutorial:
https://www.instructables.com/id/Real-time-Face-Recognition-an-End-to-end-Project/





