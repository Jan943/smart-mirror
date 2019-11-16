import cv2
import numpy as np
import os
import requests

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

API_ENDPOINT = "http://127.0.0.1:5000/"

font = cv2.FONT_HERSHEY_SIMPLEX

names = ["Jan","Michał"]

# capture video with VideoCapture and optionally set width and height

video_capture = cv2.VideoCapture(0)
# Check success
if not video_capture.isOpened():
    raise Exception("Could not open video device")
# Set properties. Each returns === True on success (i.e. correct resolution)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # read frame from camera

    # Read picture. ret === True on success
    ret, img = video_capture.read()
    #check height and width!
    #width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    #height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #print('size:', width, height)

	# convert image to gray with cvtColor

    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect faces on grayscale image using detectMultiScale from faceCascade
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20))


    # check how many faces were detected
	# # if face is detected predict face from trained ones using recognizer.predict (which takes part of image) and send post request with detected name
	# # if no face detected send empty string
    result = "empty"
    count_of_faces = len(faces)
    print("Faces detected: {}".format(count_of_faces))
    if (count_of_faces) :
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            result =  recognizer.predict(roi_gray)[[0]-1]
            print(result)
            requests.post("http://127.0.0.1:5000",data=result)
    else:
            print("empty")
            requests.post("http://127.0.0.1:5000",data="")

    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
