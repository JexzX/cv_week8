import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path ke gambar")
args = vars(ap.parse_args())

gambar = cv2.imread(args["image"])
gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Blurred", blurred)

canny = cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)