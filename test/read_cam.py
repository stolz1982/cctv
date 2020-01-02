import numpy as np
import cv2

cap = cv2.VideoCapture(0)


ret, img = cap.read()
print(img.shape)

y=200
x=200
h=150
w=150
crop = img[y:y+h, x:x+w]
cv2.imshow('Image', crop)
print(crop.shape)
print(crop.size)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame[0:0, 50:50] = rect   
    #rechteck einblenden
    #cv2.rectangle(was soll mit einem Rechteck versehen werden,x und y Korridaten in px und als letztes die Rahmen stärke in px
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
    frame = cv2.rectangle(frame,(1,1),(10,10),(0,0,255),-1)
    
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    
    cv2.imshow('UGLY',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
