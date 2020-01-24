import cv2
import time
import numpy as np
import imutils
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-o","--output",required=True,help="path to output")
ap.add_argument("-c","--codec",type=str,default="XVID",help="codecc")
ap.add_argument("-f","--fps",type=int,help='rate')

args=vars(ap.parse_args())
cap=cv2.VideoCapture(0);


fourcc=cv2.VideoWriter_fourcc(*args["codec"])
(h,w)=(None,None)
ret,frame=cap.read()

       
    print(h,w)
    #frame=imutils.resize(frame,width=420)
    
    
while(cap.isOpened()):
    ret,frame=cap.read()
    if (h,w)== (None,None):
        (h,w)=frame.shape[:2]
        writer=cv2.VideoWriter(args["output"],fourcc,args["fps"],(w,h))
        
    #print(h,w)
    writer.write(frame)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
            
