import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])

M = np.ones(gambar.shape, dtype="uint8") * 75
ditambah = cv2.add(gambar, M)
dikurang = cv2.subtract(gambar, M)

cv2.imshow("Original", gambar)
cv2.imshow("Ditambah 75", ditambah)
cv2.imshow("Dikurang 75", dikurang)
cv2.waitKey(0)