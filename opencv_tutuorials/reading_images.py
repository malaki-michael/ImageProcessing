import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt


def read_image():
    root = os.getcwd()
    imgPath = os.path.join(root,"images","peppers_color.tif")
    print(f"Image apth: {imgPath}")
    img = cv.imread(imgPath)
    if img == None:
        print("Image Not Found")
        return
    cv.imshow("img", img)
    cv.waitKey(0) # 0 means infinity


if __name__ == "__main__":
    read_image()