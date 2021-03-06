# https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
# pip3 install pillow
# pip3 install pytesseract
# sudo apt-get install tesseract-ocr

# import the necessary packages
import cv2
import imutils 
import numpy as np
from PIL import Image


path = '/home/pi/cctv/test/test8.jpeg'
y = 880
x = 1100
h = 150
w = 250

while True:

    img = cv2.imread(path)
    #definition of the REGION OF INTEREST (ROI) 
    img = img[y:y+h, x:x+w]
    cv2.imshow("ROI", img)
    
    # Rescale the image, if needed.
  #toDO --> figure out DPI and ensure more than 300 or even more for ROI
    rescaled = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("BGR2GRAY", rescaled)
    
    #Grayscal the image
    #This speeds up other following process sine we no longer have to deal with the color details when processing an image
    gray = cv2.cvtColor(rescaled, cv2.COLOR_BGR2GRAY)
    cv2.imshow("BGR2GRAY", gray)


    #filtering useless information (bluring)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    cv2.imshow("bilateralfilter", gray)
    
    #Edge Detection
    #default 30, 200
    edged = cv2.Canny(gray, 15, 80,0)
    cv2.imshow("Edge Detection", edged)
    
    #looking for contours in our images
    #sorting them from big to small and take over only 10 contours
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None

    #loop over our contours
    for c in cnts:
                # approximate the contour
                peri = cv2.arcLength(c, True)
                # 0.018 is an experimental value
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                # if our approximated contour has four points, then
                # we can assume that we have found our screen
                if len(approx) == 4:
                      screenCnt = approx
                      break 
    # Masking the part other than the number plate
    mask = np.zeros(gray.shape,np.uint8)
    cv2.imshow("mask",mask)
    #new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
    #new_image = cv2.bitwise_and(img,img,mask=mask)

    # Now crop
    #(x, y) = np.where(mask == 255)
    #(topx, topy) = (np.min(x), np.min(y))
    #(bottomx, bottomy) = (np.max(x), np.max(y))
    #cropped = gray[topx:bottomx+1, topy:bottomy+1]
    #cv2.imshow("Cropped",Cropped)
    
    #Read the number plate
 #to Do -- test -->  tesseract --psm 13 --oem 1 -l deu page.png 
    #text = pytesseract.image_to_string(cropped, config='--psm 11')
    #print("Detected Number is:",text)


    key = cv2.waitKey(1) & 0xFF
    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
    	break

# cleanup the camera and close any open windows
cv2.destroyAllWindows()
