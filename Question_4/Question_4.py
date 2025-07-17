import cv2
import numpy as np
from skimage import exposure

img = cv2.imread('/Users/nabeelnazeer/Documents/Image_Video_ProcessingLab/panda.png', 0)
local_eq = exposure.equalize_adapthist(img/255)
local_eq_img = (local_eq * 255).astype('uint8')
cv2.imwrite('local_equalized.png', local_eq_img)
print('Local histogram equalization saved as local_equalized.png')
