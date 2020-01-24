import argparse
import cv2
import imutils

#instantiate the object as ap
ap=argparse.ArgumentParser()
ap.add_argument("-i","--input",required=True,help="path to input image")
ap.add_argument("-o","--output",required=True,help="output path")

args=vars(ap.parse_args())

#here 2 argumnets are passed one as input and another is output

image=cv2.imread(args["input"])
#path to the image is given from command line argument
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite(args["output"], gray)
                
                
                
