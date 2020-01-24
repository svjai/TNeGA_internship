import cv2
import numpy as np #for reading the frames as numpy ndarray

c=cv2.VideoCapture(0);#domain index of camera (any_type usually 0)
print(type(c))
while True:

    ret,frame=c.read() # Grabs and retrieves frames and decode
    if ret == True:
        
        cv2.imshow("frame",frame)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #for checking the graycsale image
    #print("ra",ret,frame)
        cv2.imshow("fra",frame)  #used to show the frame read by the imread 
        if cv2.waitKey(1) & 0xFF==ord('q'): #waitkey-keyboard binding function, wait till delay time to check pressed key if not it will return -1 
            print(ord('q'))
            print(0xFF)           
            print(cv2.waitKey(1))
            print(cv2.waitKey(1) & 0xFF==ord('q'))
            break
#print(cv2.waitKey(1) & 0xFF==ord('q'))    
#c2 = cv2.VideoCapture(0)
c.release() #deallcates the memory used for capturing the frames and the pointers used
'''
so that we can access the camera or it will opened or allocated
'''
cv2.destroyAllWindows() #used to destroy the windows which we used to show the fra and frame here

