import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = '/Users/nabeelnazeer/Documents/Image_Video_ProcessingLab/panda.png'
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError(f'Image not found at {img_path}')

rows, cols = img.shape[:2]

# a. Translation
M_translate = np.float32([[1, 0, 100], [0, 1, 50]])  # shift right by 100, down by 50
translated = cv2.warpAffine(img, M_translate, (cols, rows))
cv2.imwrite('translated.png', translated)

# b. Rotation
M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)  # rotate 45 degrees
rotated = cv2.warpAffine(img, M_rotate, (cols, rows))
cv2.imwrite('rotated.png', rotated)

# c. Scaling
scaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('scaled.png', scaled)

# d. Skewing (Shearing)
M_skew = np.float32([[1, 0.5, 0], [0.2, 1, 0]])
skewed = cv2.warpAffine(img, M_skew, (int(cols*1.5), int(rows*1.2)))
cv2.imwrite('skewed.png', skewed)

# Display all results
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original')
axs[0, 0].axis('off')
axs[0, 1].imshow(cv2.cvtColor(translated, cv2.COLOR_BGR2RGB))
axs[0, 1].set_title('Translated')
axs[0, 1].axis('off')
axs[0, 2].imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
axs[0, 2].set_title('Rotated')
axs[0, 2].axis('off')
axs[1, 0].imshow(cv2.cvtColor(scaled, cv2.COLOR_BGR2RGB))
axs[1, 0].set_title('Scaled')
axs[1, 0].axis('off')
axs[1, 1].imshow(cv2.cvtColor(skewed, cv2.COLOR_BGR2RGB))
axs[1, 1].set_title('Skewed')
axs[1, 1].axis('off')
axs[1, 2].axis('off')
plt.tight_layout()
plt.show()
print('All geometrical transformation results saved in Question_6 folder.')
