import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
cv2.imshow("Gambar Asli", gambar)

# Crop bagian tertentu dari gambar
terpotong = gambar[50:150, 100:200]
cv2.imshow("Gambar Terpotong", terpotong)

# Ubah region tertentu jadi warna hijau
gambar[50:150, 100:200] = (0, 255, 0)
cv2.imshow("Gambar dengan Kotak Hijau", gambar)

cv2.waitKey(0)