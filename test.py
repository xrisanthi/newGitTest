from scipy import misc
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# read an image
image = misc.imread("C:\\Users\c.iakovidou\Desktop\kohle_akt_1_by_m_schoessler-d90amzz.jpg", mode="L")
print(type(image[3 ,1]))
print(image.min())
print(image.max())
#get the histogram of the image

hist, num_of_bins = np.histogram(image, bins=255, range=(0,255))
# print(num_of_bins)
print(hist)
print("the size of is", image.shape )

im_min = image.min()
im_max = image.max()
im_mean = image.mean()

plt.plot(hist)
plt.show()
