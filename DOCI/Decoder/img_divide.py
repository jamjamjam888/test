import cv2
import glob
import numpy as np
filepath = "img/image_dst2.png"
filename = glob.glob(filepath)

for files in filename:
    img = cv2.imread(files)
    Blue,Green,Red = cv2.split(img)
    cv2.imwrite("img/Blue.png",Blue)
    cv2.imwrite("img/Green.png",Green)
    cv2.imwrite("img/Red.png",Red)