import cv2
import time

img_rgb = cv2.imread("picture/2794-3.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_gray = cv2.medianBlur(img_gray, 5)
img_edge = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
         cv2.THRESH_BINARY, blockSize=3, C=2)
cv2.imwrite("result1.jpg", img_edge)

