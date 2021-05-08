import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

image = imageio.imread("../BilderV2/unbearbeitet.png")
image = image.astype('float32')
plt.imshow(image)
plt.show()

schwarz = image[:,0:50]
grau1 = image[:,150:200]
grau2 = image[:,300:350]
grau3 = image[:,400:450]
weiß = image[:,550:600]

print(weiß)