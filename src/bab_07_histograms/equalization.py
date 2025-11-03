import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(gray)

cv2.imshow("Original Grayscale", gray)
cv2.imshow("Equalized", equalized)
cv2.waitKey(0)