import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
print("lebar: {} piksel".format(gambar.shape[1]))
print("tinggi: {} piksel".format(gambar.shape[0]))
print("channel: {}".format(gambar.shape[2]))

cv2.imshow("Gambar", gambar)
cv2.waitKey(0)

cv2.imwrite("gambar_baru.jpg", gambar)
print("gambar disimpan sebagai gambar_baru.jpg")
cv2.destroyAllWindows()