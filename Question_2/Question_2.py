import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('/Users/nabeelnazeer/Documents/Image_Video_ProcessingLab/panda.png', 0)
plt.hist(img.ravel(), 256, [0,256])
plt.title('Histogram')
plt.savefig('histogram.png')
print('Histogram saved as histogram.png')
