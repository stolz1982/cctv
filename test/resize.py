import cv2
import numpy
px = 50
image = cv2.imread("img_denoised.jpg")
r = 100.0 / image.shape[1]
dim = (px, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#cv2.imshow("resized", resized)
file = "resized_%s.jpg" %(px)
#“{} {} is {} years old.“ format(fname, lname, age)
cv2.imwrite(file, resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
