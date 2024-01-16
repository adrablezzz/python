import cv2 as cv
import numpy as np

def imshow(img):
  cv.imshow('image', img)
  cv.waitKey(0)
  cv.destroyAllWindows()

img1 = cv.imread('x.png')
img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
# imshow(img1_gray)
img1_np = np.array(img1_gray) / 255
print(img1_np)