import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/Users/nabeelnazeer/Documents/Image_Video_ProcessingLab/panda.png', 0)
equalized = cv2.equalizeHist(img)
cv2.imwrite('equalized.png', equalized)
plt.hist(equalized.ravel(), 256, [0,256])
plt.title('Equalized Histogram')
plt.savefig('equalized_histogram.png')
print('Equalized image and histogram saved.')
