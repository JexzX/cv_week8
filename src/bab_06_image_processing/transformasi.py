import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])

def translasi(gambar, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    bergeser = cv2.warpAffine(gambar, M, (gambar.shape[1], gambar.shape[0]))
    return bergeser

def rotasi(gambar, sudut, tengah=None, skala=1.0):
    (h, w) = gambar.shape[:2]
    if tengah is None:
        tengah = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(tengah, sudut, skala)
    diputar = cv2.warpAffine(gambar, M, (w, h))
    return diputar

# Translasi
geser_kanan_bawah = translasi(gambar, 50, 50)
geser_kiri_atas = translasi(gambar, -50, -50)

# Rotasi
putar_45 = rotasi(gambar, 45)
putar_90 = rotasi(gambar, -90)

cv2.imshow("Original", gambar)
cv2.imshow("Geser Kanan Bawah", geser_kanan_bawah)
cv2.imshow("Geser Kiri Atas", geser_kiri_atas)
cv2.imshow("Putar 45 Derajat", putar_45)
cv2.imshow("Putar -90 Derajat", putar_90)
cv2.waitKey(0)