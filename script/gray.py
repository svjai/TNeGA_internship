import cv2
import numpy
cap=cv2.VideoCapture(0);
h1,w1=None,None
percent=75
while(True):
    ret,frame = cap.read()
    print(frame.shape)
    if ret == True:
        cv2.imshow("shape",frame)
        w1 = int(frame.shape[1] * percent/ 100)
        h1 = int(frame.shape[0] * 100/ 100)
        dim=(w1,h1)
       
        frame=cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
        print(frame.shape)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



'''
        print(frame.shape)
        h1, w1 = frame.shape[:2]
        frame = frame[int(0):int(h1), int(w1/4):int(w1*3/4)]
        print(frame.shape)
'''
        
        
        #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("gray",frame)
'''
    else:
        print('error')
        break
'''
cap.release()
cv2.destroyAllWindows()
