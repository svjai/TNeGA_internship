import cv2
import numpy as np
import time
import imutils 



cap=cv2.VideoCapture("gray.avi");

tot=0
start=time.time()
#print(start)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        cv2.imshow("fps",frame)
        tot+=1
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
    else:
        break
print(tot/(time.time()-start))
#print(time.time())
print(tot)
#print(cap.get(5))
cap.release()
cv2.destroyAllWindows()
