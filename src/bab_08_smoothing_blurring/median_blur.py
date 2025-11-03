import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
cv2.imshow("Original", gambar)

median3 = cv2.medianBlur(gambar, 3)
median5 = cv2.medianBlur(gambar, 5)
median7 = cv2.medianBlur(gambar, 7)

cv2.imshow("Median 3", median3)
cv2.imshow("Median 5", median5)
cv2.imshow("Median 7", median7)
cv2.waitKey(0)