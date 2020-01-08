# https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
# pip3 install pillow
# pip3 install pytesseract
# sudo apt-get install tesseract-ocr

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os


while True:
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done, thresh is default and alternately you can use blur")
    args = vars(ap.parse_args())

    # load the example image and convert it to grayscale
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the
    # image
    if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif args["preprocess"] == "blur":
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
    dim = (640, 480)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    #cv2.imshow("Image", image)
    gray = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
    #cv2.imshow("Output", gray)


    key = cv2.waitKey(1) & 0xFF
    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
    	break

# cleanup the camera and close any open windows
cv2.destroyAllWindows()

