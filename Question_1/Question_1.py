import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# a. Read an image
img_path = '/Users/nabeelnazeer/Documents/Image_Video_ProcessingLab/panda.png'
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError(f'Image not found at {img_path}')

# b. Get the image information
info = {
    'shape': img.shape,
    'dtype': img.dtype,
    'size': img.size
}
print('Image Info:', info)

# c. Find the compression ratio for the copied image
copy_path = 'panda_copy.jpg'
cv2.imwrite(copy_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
orig_size = os.path.getsize(img_path)
copy_size = os.path.getsize(copy_path)
compression_ratio = orig_size / copy_size if copy_size else None
print('Compression Ratio:', compression_ratio)

# d. Display the negative of an image
negative = 255 - img
cv2.imwrite('negative.png', negative)
print('Negative image saved as negative.png')

# Display the negative image using matplotlib
plt.imshow(cv2.cvtColor(negative, cv2.COLOR_BGR2RGB))
plt.title('Negative Image')
plt.axis('off')
plt.show()
