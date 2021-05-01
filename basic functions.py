import cv2
import numpy
path = "/Applications/PyCharm CE.app/Contents/Resources/smarty.jpg"
kernel = numpy.ones((5,5),numpy.uint8)
img = cv2.imread(path)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgray,(15,15),0)
imgcanny = cv2.Canny(imgblur,50,50)
#if we increase the kernel size in blur, the image gets more blurred
#as higher the threshold values in canny, more boundaries we will see in image
imgdilation = cv2.dilate(imgcanny,kernel,iterations=1)
#the effect increases with increase in iterations
imgerotion = cv2.erode(imgdilation,kernel,iterations=1)


cv2.imshow("smarty",img)
cv2.imshow("grayscale",imgray)
cv2.imshow("blur",imgblur)
cv2.imshow("canny",imgcanny)
cv2.imshow("dilate",imgdilation)
cv2.imshow("erode",imgerotion)
cv2.waitKey(0)