import cv2
import numpy as np


img = cv2.imread('j-noise.png',0)

kernel = np.ones((5, 5), np.uint8)
result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow("Source", img)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
