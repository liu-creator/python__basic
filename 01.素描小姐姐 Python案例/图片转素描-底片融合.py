import cv2
import numpy as np
 
 
def rgb_to_sketch(src_image, dst_image):
    img_rgb = cv2.imread(src_image_name)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)
    img_blend = cv2.divide(img_gray, img_blur, scale=255)  # 除法运算，改变的是每个像素的颜色深度
    cv2.imwrite(dst_image_name, img_blend)
 
 
if __name__ == '__main__':
    src_image_name = '2794-3.jpg'
    dst_image_name = 'trans2.jpg'
    rgb_to_sketch(src_image, dst_image)