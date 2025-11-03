import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
cv2.imshow("Original", gambar)

mask = np.zeros(gambar.shape[:2], dtype="uint8")
(cX, cY) = (gambar.shape[1] // 2, gambar.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask Persegi", mask)

masked = cv2.bitwise_and(gambar, gambar, mask=mask)
cv2.imshow("Hasil Masking Persegi", masked)

mask2 = np.zeros(gambar.shape[:2], dtype="uint8")
cv2.circle(mask2, (cX, cY), 100, 255, -1)
cv2.imshow("Mask Lingkaran", mask2)

masked2 = cv2.bitwise_and(gambar, gambar, mask=mask2)
cv2.imshow("Hasil Masking Lingkaran", masked2)
cv2.waitKey(0)