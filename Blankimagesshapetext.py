import cv2
import numpy as np

img = np.zeros((1024,1024,3),np.uint8)
print(img)
cv2.line(img,(0,0),(880,1024),(255,0,0),2)
cv2.circle(img,(40,40),10,(0,0,255),cv2.FILLED)
cv2.rectangle(img,(100,200),(300,400),(255,255,0),5)
cv2.putText(img,"YOYO",(900,700),cv2.FONT_ITALIC,1,(0,150,0),1)
cv2.imshow("image",img)
cv2.waitKey(0)