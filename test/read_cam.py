import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #rechteck einblenden
    frame = cv2.rectangle(frame,(150,150),(300,300),(255,0,0),2)
    
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Display the resulting frame

    #cv2.imshow('frame',gray)
    cv2.imshow('UGLY',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
