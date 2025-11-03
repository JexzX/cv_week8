import numpy as np
import cv2

persegi = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(persegi, (50, 50), (250, 250), 255, -1)
cv2.imshow("Persegi", persegi)

lingkaran = np.zeros((300, 300), dtype="uint8")
cv2.circle(lingkaran, (150, 150), 100, 255, -1)
cv2.imshow("Lingkaran", lingkaran)

bitwiseAND = cv2.bitwise_and(persegi, lingkaran)
bitwiseOR = cv2.bitwise_or(persegi, lingkaran)
bitwiseXOR = cv2.bitwise_xor(persegi, lingkaran)
bitwiseNOT = cv2.bitwise_not(lingkaran)

cv2.imshow("AND", bitwiseAND)
cv2.imshow("OR", bitwiseOR)
cv2.imshow("XOR", bitwiseXOR)
cv2.imshow("NOT", bitwiseNOT)
cv2.waitKey(0)