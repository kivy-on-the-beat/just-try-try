
import cv2 
import numpy as np 
img = cv2.imread("R-C.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2) 
contours, hierarchy = cv2.findContours(gray,cv2.RETR_LIST ,cv2.CHAIN_APPROX_SIMPLE)  
maxIndex = 0  
maxArea = 0  
for i in range(len(contours)):    
    area = cv2.contourArea(contours[i])    
    if (area > maxArea):        
        maxArea = area        
        maxIndex=i     
x,y,w,h=cv2.boundingRect(contours[maxIndex])           						    
# Draw a rectangle around the plate           		 
img=cv2.rectangle(img , (x , y), (x + w , y + h), (0 , 255 , 0), 2)          
# Crop out the plate from original image          
plateImg=img[y:y+h , x:x+w]         
# Show the output image           
cv2.imshow("Plate" , plateImg)
cv2.waitKey(0)
# Wait for user to press any key           

