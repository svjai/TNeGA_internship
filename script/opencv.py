import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread(r"C:\Users\TNeGA\Desktop\opencv\samples\data\rubberwhale1.png",-1)
cv2.imshow("jai",img)
color=('b','g','r')
for i,col in enumerate(color):
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
