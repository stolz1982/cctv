# https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
# pip3 install pillow
# pip3 install pytesseract
# sudo apt-get install tesseract-ocr

# import the necessary packages
import cv2

path = '/home/pi/cctv/test/test8.jpeg'
y = 880
x = 1100
h = 150
w = 250

while True:

    img = cv2.imread(path)
    img = img[y:y+h, x:x+w]
    cv2.imshow("Output", img)
    
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
    	break

# cleanup the camera and close any open windows
cv2.destroyAllWindows()
