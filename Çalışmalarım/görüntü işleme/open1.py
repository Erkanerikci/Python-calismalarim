import cv2 
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("Griresim.jpg",0)
plt.imshow(image, cmap="gray",interpolation="bicubic")
plt.xticks([])
plt.yticks([])
plt.show()
