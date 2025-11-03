import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
cv2.imshow("Original", gambar)

blur3 = cv2.blur(gambar, (3, 3))
blur5 = cv2.blur(gambar, (5, 5))
blur7 = cv2.blur(gambar, (7, 7))

cv2.imshow("Blur 3x3", blur3)
cv2.imshow("Blur 5x5", blur5)
cv2.imshow("Blur 7x7", blur7)
cv2.waitKey(0)