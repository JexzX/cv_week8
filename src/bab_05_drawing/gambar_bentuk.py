import numpy as np
import cv2

kanvas = np.zeros((300, 300, 3), dtype="uint8")

hijau = (0, 255, 0)
cv2.line(kanvas, (0, 0), (300, 300), hijau)
cv2.imshow("Garis Hijau", kanvas)
cv2.waitKey(0)

merah = (0, 0, 255)
cv2.line(kanvas, (300, 0), (0, 300), merah, 3)
cv2.imshow("Garis Merah", kanvas)
cv2.waitKey(0)

cv2.rectangle(kanvas, (10, 10), (60, 60), hijau)
cv2.imshow("Persegi Hijau", kanvas)
cv2.waitKey(0)

cv2.rectangle(kanvas, (50, 200), (200, 225), merah, 5)
cv2.imshow("Persegi Merah", kanvas)
cv2.waitKey(0)

biru = (255, 0, 0)
cv2.rectangle(kanvas, (200, 50), (225, 125), biru, -1)
cv2.imshow("Persegi Biru Solid", kanvas)
cv2.waitKey(0)

cv2.destroyAllWindows()