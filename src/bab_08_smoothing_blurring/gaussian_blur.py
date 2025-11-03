import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
cv2.imshow("Original", gambar)

gauss3 = cv2.GaussianBlur(gambar, (3, 3), 0)
gauss5 = cv2.GaussianBlur(gambar, (5, 5), 0)
gauss7 = cv2.GaussianBlur(gambar, (7, 7), 0)

cv2.imshow("Gaussian 3x3", gauss3)
cv2.imshow("Gaussian 5x5", gauss5)
cv2.imshow("Gaussian 7x7", gauss7)
cv2.waitKey(0)