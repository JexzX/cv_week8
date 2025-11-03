import numpy as np
import cv2

kanvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (kanvas.shape[1] // 2, kanvas.shape[0] // 2)
putih = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(kanvas, (centerX, centerY), r, putih)

cv2.imshow("Lingkaran Konsentris", kanvas)
cv2.waitKey(0)

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    cv2.circle(kanvas, tuple(pt), radius, color, -1)

cv2.imshow("Lingkaran Acak", kanvas)
cv2.waitKey(0)