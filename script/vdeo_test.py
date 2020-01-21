import cv2
import datetime
cap=cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,1280)
cap.set(4,620)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(5))
cap.set(5,10)
print(cap.get(5))
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
      
      font=cv2.FONT_HERSHEY_SIMPLEX
      
      d=str(datetime.datetime.now())
      text= 'Width: ' + str(cap.get(3))+' Height: ' + str(cap.get(4)) +'Time:' + d
      frame=cv2.putText(frame,text,(10,50),font,.5,(0,255,255),1)
      
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#r'C:\Users\TNeGA\Desktop\trimmed\kushal_server\201981\67811_test.avi'
#
