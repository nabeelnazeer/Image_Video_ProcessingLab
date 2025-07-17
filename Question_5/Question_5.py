import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/nabeelnazeer/Documents/Image_Video_ProcessingLab/panda.png', 0)

# a. Brightness enhancement
bright = cv2.convertScaleAbs(img, alpha=1, beta=50)
cv2.imwrite('bright.png', bright)

# b. Contrast enhancement
contrast = cv2.convertScaleAbs(img, alpha=2, beta=0)
cv2.imwrite('contrast.png', contrast)

# c. Complement of an image
complement = 255 - img
cv2.imwrite('complement.png', complement)

# d. Bi-level or binary contrast enhancement
_, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
cv2.imwrite('binary.png', binary)

# e. Brightness slicing
_, sliced = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
cv2.imwrite('sliced.png', sliced)

# f. Low-pass filtering
low_pass = cv2.GaussianBlur(img, (5,5), 0)
cv2.imwrite('low_pass.png', low_pass)

# g. High-pass filtering
kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
high_pass = cv2.filter2D(img, -1, kernel)
cv2.imwrite('high_pass.png', high_pass)

print('All enhancement outputs saved.')
