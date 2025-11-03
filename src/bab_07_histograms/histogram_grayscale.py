import argparse
import cv2
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histogram Grayscale")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)