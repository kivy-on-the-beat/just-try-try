# First, we import the necessary libraries: OpenCV and NumPy
import cv2 
import numpy as np 
# Next, we read in an image file named "R-C.jpg" using OpenCV's imread function
img = cv2.imread("R-C.jpg")
# We then convert the image to grayscale using cvtColor function
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# apply an adaptive threshold to the grayscale image to create a binary image
gray = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2) 
# We find contours in the binary image using findContours function
contours, hierarchy = cv2.findContours(gray,cv2.RETR_LIST ,cv2.CHAIN_APPROX_SIMPLE)  
# initialize variables to keep track of the contour with the largest area
maxIndex = 0  
maxArea = 0  
# loop through all contours to find the one with the largest area
for i in range(len(contours)):    
    area = cv2.contourArea(contours[i])    
    if (area > maxArea):        
        maxArea = area        
        maxIndex=i     
# get the bounding rectangle of the contour with largest area     
x,y,w,h=cv2.boundingRect(contours[maxIndex])           						    
# Draw a rectangle around the plate           		 
img=cv2.rectangle(img , (x , y), (x + w , y + h), (0 , 255 , 0), 2)          
# Crop out the plate from original image          
plateImg=img[y:y+h , x:x+w]         
# Show the output image           
cv2.imshow("Plate" , plateImg)
cv2.waitKey(0)
print("thank you")
# Wait for user to press any key           
