#Importing OpenCV Library for basic image processing functions
import cv2
import urllib.request #para abrir y leer URL
# Numpy for array related functions
import numpy as np
# Dlib for deep learning based Modules and face landmark detection
import dlib
#face_utils for basic operations of conversion
from imutils import face_utils

from functions.euclidian_distance import compute

from functions.blinkcheck import blinked

# import required module
from playsound import playsound

from time import time, sleep


#Initializing the face detector and landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#status marking for current state
sleep = 0
drowsy = 0
active = 0
status=""
color=(0,0,0)


while True:
    # Initializing the camera and taking the instance
    winName = 'ESP32 CAMERA'
    cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
    url = 'http://192.168.249.86/cam-hi.jpg'
    imgResponse = urllib.request.urlopen(url)  # we open the URL
    imgNp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
    cap = cv2.imdecode(imgNp, -1)  # we decode
    # cap = cv2.VideoCapture(0)
    #_, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)



    faces = detector(gray)
    #detected face in faces array
    #face_frame = frame.copy()
    face_frame = cap.copy()

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()


        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        #The numbers are actually the landmarks which will show eye
        left_blink = blinked(landmarks[36],landmarks[37],
        	landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42],landmarks[43],
        	landmarks[44], landmarks[47], landmarks[46], landmarks[45])

        #Now judge what to do for the eye blinks
        if(left_blink==0 or right_blink==0):
        	sleep+=1
        	# drowsy=0
        	active=0
        	if(sleep>6):
        		status="SLEEPING !!!"
        		color = (255,255,255)

        # elif(left_blink==1 or right_blink==1):
        # 	sleep=0
        # 	active=0
        # 	drowsy+=1
        # 	if(drowsy>6):
        # 		status="Drowsy !"
        # 		color = (255,255,255)

        else:
        	drowsy=0
        	sleep=0
        	active+=1
        	if(active>6):
        		status="Active :)"
        		color = (0,255,0)

        #cv2.putText(frame, status, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)
        cv2.putText(cap, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
        print(status)
        if(status=="SLEEPING !!!"):

            playsound('Sound Effect Beep Alert Loop.wav')




        for n in range(0, 68):
        	(x,y) = landmarks[n]
        	cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    # cv2.imshow("Frame", frame)
    cv2.imshow("Frame", cap)
    cv2.imshow("Result of detector", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
      	break