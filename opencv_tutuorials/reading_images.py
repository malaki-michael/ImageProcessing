import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage import io


def read_image():
    root = os.getcwd()
    imgPath = os.path.join(root,"images","lena_color_256.tif")
    print(f"Current directory: {root}")
    print(f"Image apth: {imgPath}")
    img = io.imread(imgPath)
    if img == None:
        print("Image Not Found")
        return
    io.imshow("img", img)
    plt.show()
    #cv.waitKey(0) # 0 means infinity


if __name__ == "__main__":
    read_image()