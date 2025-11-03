import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
cv2.imshow("Gambar Asli", gambar)

(b, g, r) = gambar[0, 0]
print("Pixel di (0, 0) - Merah: {}, Hijau: {}, Biru: {}".format(r, g, b))

gambar[0, 0] = (0, 0, 255)
(b, g, r) = gambar[0, 0]
print("Pixel di (0, 0) - Merah: {}, Hijau: {}, Biru: {}".format(r, g, b))

cv2.imshow("Gambar Diubah", gambar)
cv2.waitKey(0)