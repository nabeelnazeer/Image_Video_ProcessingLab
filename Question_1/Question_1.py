import cv2
import numpy as np
from PIL import Image
import os

# Read image
img_path = '/Users/nabeelnazeer/Documents/Image_Video_ProcessingLab/panda.png'
img = cv2.imread(img_path)

# Get image information
info = {
    'shape': img.shape,
    'dtype': img.dtype,
    'size': img.size
}
print('Image Info:', info)

# Save a copy and calculate compression ratio
copy_path = 'panda_copy.jpg'
cv2.imwrite(copy_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
orig_size = os.path.getsize(img_path)
copy_size = os.path.getsize(copy_path)
compression_ratio = orig_size / copy_size if copy_size else None
print('Compression Ratio:', compression_ratio)

# Display negative of image
negative = 255 - img
cv2.imwrite('negative.png', negative)
print('Negative image saved as negative.png')
