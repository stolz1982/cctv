#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#basic-ops
import numpy as np
import cv2

img = cv2.imread('/home/user01/cctv/test/test.jpg')
#zugriff auf die Pixel in Reihe 100 und Spalte 100
px = img[100,100]
#ausdruck der BGR Werte
print px

#zugriff nur die auf die blauen Pixel
px = img[100, 100, 0]
print px

#zugriff nur die auf die gruenen Pixel
px = img[100, 100, 1]
print px

#zugriff nur die auf die roten Pixel
px = img[100, 100, 2]
print px

img[100,100] = [123,234,255]
print img[100,100]

# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
px = img.item(10,10,2)
print px


#metadata of picture
print img.shape
#shows the numbers of rows, columns and type of picture, if function returns the r and c olny then it is a gray scale picture

#shows the datatype of the picture
print img.dtype

#Region of IMAGE
#set the ROI of a square defines by the matrix values hereafter
ROI = img[280:340, 330:390]
#like a copy of the hereabove mentioned region
img[273:333, 100:160] = ROI


#Rahmen um ein BILD erstellen
#from matplotlib import pyplot as plt

#BLUE = [255,0,0]
#constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
#plt.imshow(constant,'gray'),plt.title('CONSTANT')
#plt.show





