# https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
# pip3 install pillow
# pip3 install pytesseract
# sudo apt-get install tesseract-ocr

# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os

path = 'test8.jpeg'
dim = (640, 480)
y = 925
x = 1175
h = 45
w = 85
#processing = 'blur'
processing = 'thresh'


while True:

    img = cv2.imread(path)
    img = img[y:y+h, x:x+w]
    img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,42)
    img_name = "img_denoised_%s.jpg" %(h)
    cv2.imwrite(img_name,img)
    
    # load the example image and convert it to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the
    # image
    if processing == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif processing == "blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)

    # show the output images
#    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Image", img)
#    gray = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Output", gray)
    
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
    	break

# cleanup the camera and close any open windows
cv2.destroyAllWindows()

