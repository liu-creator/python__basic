import requests
import re
import os
import time
import cv2
import numpy as np
 
 
def rgb_to_sketch(src_image, dst_image):
    img_rgb = cv2.imread(src_image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)
    img_blend = cv2.divide(img_gray, img_blur, scale=255)  
    cv2.imwrite(dst_image, img_blend)

def get_jpg_urls(urllist):
    headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
        }
    for url in urllist:
        html = requests.get(url, headers=headers)
        urltext = requests.get(url, headers=headers).text
        jpgurls = re.findall(r'[a-zA-z]+://[^\s]*jpg"', urltext)
        jpgname = re.split('\\.|/', url)[-2]
        save_jpg(jpgurls, jpgname)

def save_jpg(jpgurls, jpgname):
    try:
        os.mkdir('picture')
    except FileExistsError:
        print('文件夹已存在')
    for i in range(len(jpgurls)):
        path = 'picture/{}-{}.jpg'.format(jpgname, str(i))  
        jpg = requests.get(jpgurls[i]).content
        time.sleep(1)
        with open(path, 'wb') as f:
            f.write(jpg)
        rgb_to_sketch(path, path)


def main():
    idlist = ['id1', 'id2']
    urllist = ['http://www.waxjj.cn/'+x+'.html' for x in idlist]
    jpgurls = get_jpg_urls(urllist)

if __name__ == '__main__':
    main()