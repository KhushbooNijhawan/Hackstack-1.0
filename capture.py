import cv2

videoCaptureObject = cv2.VideoCapture(0)
result = 1
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture" + str(result) + ".jpg",frame)
    result +=1
videoCaptureObject.release()
cv2.destroyAllWindows()