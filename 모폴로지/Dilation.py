import cv2
import numpy as np


img = cv2.imread('j.png',0)

kernel = np.ones((5, 5), np.uint8)
result = cv2.dilate(img, kernel, iterations = 1)

cv2.imshow("Source", img)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
