import cv2  
import numpy as np 

vid = cv2.VideoCapture(0)
first_frame=None
while(vid.isOpened):
    ret,frame=vid.read()

    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(21,21),0)
        if first_frame is None:
            first_frame=gray
            continue

        delta_frame=cv2.absdiff(first_frame,gray) #Calculates the difference between first frame and other frames
        
        #Provides a threshold value,such that it will convert the difference value with less than 30 to black.
        #If the difference is greater than 30 it willconvert those to white
        thresh_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
        thresh_delta=cv2.dilate(thresh_delta,None,iterations=0)
        #Define contour area . Basically , add the borders
        (cnts,_) = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        
        for contours in cnts:
            if cv2.contourArea(contours)<1000: #Removes noise and shadows. Basically it will keep the area greater than 1000 pixels.
                continue
            (x,y,w,h) = cv2.boundingRect(contours)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.imshow("Main Frame",frame) 
        cv2.imshow("Capturing",gray)
        cv2.imshow('delta',delta_frame)
        cv2.imshow('thresh',thresh_delta)
        if cv2.waitKey(1) == ord('q'):
            break

vid.release()
cv2.destroyAllWindows