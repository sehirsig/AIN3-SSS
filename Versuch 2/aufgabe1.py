import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

image = imageio.imread("../BilderV2/unbearbeitet.png")
#image = image.astype('float32')

plt.imshow(image)
plt.show()

schwarzbeginn = 0
grau1beginn = 2000
grau2beginn = 4000
grau3beginn = 6000
weißbeginn = 8000

schwarz = image[schwarzbeginn:grau1beginn - 1]
grau1 = image[grau1beginn:grau2beginn - 1]
grau2 = image[grau2beginn:grau3beginn - 1]
grau3 = image[grau3beginn:weißbeginn - 1]
weiß = image[weißbeginn:image.size]