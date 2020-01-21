import cv2
cap=cv2.VideoCapture(0);
#print("before",cap.get(3))
#print("sameBefore",cap.get(4))
fourcc=cv2.VideoWriter_fourcc(*'XVID')
first_jai=cv2.VideoWriter('video_jai.avi', fourcc ,5.0, (640,480))
while(True):
  ret, frame = cap.read()
  if ret == True:
      print(cap.get(3))
      print(cap.get(4))
      first_jai.write(frame)

      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  else:
      print("error")
      break
cap.release()
first_jai.release()
cv2.destroyAllWindows()
#r'C:\Users\TNeGA\Desktop\trimmed\kushal_server\201981\67811_test.avi'
#
