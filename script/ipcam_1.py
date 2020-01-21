import cv2
cap=cv2.VideoCapture('rtsp://admin:admin123@192.168.4.151');

fourcc=cv2.VideoWriter_fourcc(*'XVID')
jai=cv2.VideoWriter('ip_first.avi', fourcc ,30.0, (int(cap.get(3)), int(cap.get(4))))


while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
      
      jai.write(frame)
      cv2.imshow('frs',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
jai.release()
cv2.destroyAllWindows()
#r'C:\Users\TNeGA\Desktop\trimmed\kushal_server\201981\67811_test.avi'
#
'''import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://admin:admin123@192.168.4.151')
print(cap.get(3))
print(cap.get(4))
print(cap.get(5))
while(cap.isOpened()):

    ret, frame = cap.read()
    cv2.imshow('FRS',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
