import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])

def resize(gambar, lebar=None, tinggi=None):
    dim = None
    (h, w) = gambar.shape[:2]
    
    if lebar is None and tinggi is None:
        return gambar
    
    if lebar is None:
        r = tinggi / float(h)
        dim = (int(w * r), tinggi)
    else:
        r = lebar / float(w)
        dim = (lebar, int(h * r))
    
    resized = cv2.resize(gambar, dim, interpolation=cv2.INTER_AREA)
    return resized

# Resize
kecil_lebar = resize(gambar, lebar=150)
kecil_tinggi = resize(gambar, tinggi=100)

# Flip
flip_horizontal = cv2.flip(gambar, 1)
flip_vertikal = cv2.flip(gambar, 0)
flip_keduanya = cv2.flip(gambar, -1)

cv2.imshow("Original", gambar)
cv2.imshow("Resize Lebar 150", kecil_lebar)
cv2.imshow("Resize Tinggi 100", kecil_tinggi)
cv2.imshow("Flip Horizontal", flip_horizontal)
cv2.imshow("Flip Vertikal", flip_vertikal)
cv2.imshow("Flip Keduanya", flip_keduanya)
cv2.waitKey(0)