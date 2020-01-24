import cv2
import imutils
import time
import uuid

cap = cv2.VideoCapture(0)
start=time.time()
tot=0
h = None
w = None
video = None
while True:
    r,f = cap.read()
    if r!= True:
        print('No feed')
        break
    resized_frame = imutils.resize(f, width = 480)
    if h == None:
        h,w = resized_frame.shape[:2]
        video = cv2.VideoWriter(f'{uuid.uuid4().hex}.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20, (int(w), int(h)))
    video.write(resized_frame)
    cv2.imshow('frame', resized_frame)
    tot+=1

    key = cv2.waitKey(1000) & 0xFF
    if key == ord('q'):
        break
print("fps{}".format(tot/(time.time()-start)))
cap.release()
video.release()
cv2.destroyAllWindows()


        

    
