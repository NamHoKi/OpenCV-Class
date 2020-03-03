import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('LenaRGB.bmp',cv2.IMREAD_GRAYSCALE)

# 일반 Blur
dst1 = cv2.blur(img,(7,7))
cv2.imshow('Nomal',dst1)

# GaussianBlur
dst2 = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('Gaussian',dst2)

# Median Blur
dst3 = cv2.medianBlur(img,9)
cv2.imshow('Median',dst3)

# Bilateral Filtering
dst4 = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral',dst4)
cv2.waitKey()
cv2.destroyAllWindows()

# images = [img,dst1,dst2,dst3,dst4]
# titles=['Original','Blur(7X7)','Gaussian Blur(5X5)','Median Blur','Bilateral']
#
# for i in range(5):
#     plt.subplot(3,2,i+1),plt.imshow(images[i]),plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
#
# plt.show()
