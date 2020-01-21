import numpy as np
import cv2
cap = cv2.VideoCapture('rtsp://admin:admin123@192.168.4.151');
fourcc=cv2.VideoWriter_fourcc(*'XVID')
jai=cv2.VideoWriter('ip_scale3.avi', fourcc ,20.0, (int(cap.get(3)), int(cap.get(4))))
scaling_factorx=.5
scaling_factory=.5

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:
        jai.write(frame)
        frame=cv2.resize(frame,None,fx=scaling_factorx,fy=scaling_factory,interpolation=cv2.INTER_AREA)
        cv2.imshow('FRS',frame)
        print(cap.get(3))
        print(cap.get(4))
#print(cap.get(5))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
jai.release()
cv2.destroyAllWindows()
