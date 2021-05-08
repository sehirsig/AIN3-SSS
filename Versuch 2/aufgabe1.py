import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

image = imageio.imread("../BilderV2/unbearbeitet.png")
image = image.astype('float32')
plt.imshow(image)
plt.show()

schwarzbeginn = 0
grau1beginn = 2000
grau2beginn = 4000
grau3beginn = 6000
weißbeginn = 8000

schwarz = image[:,0:50]
grau1 = image[:,150:200]
grau2 = image[:,300:350]
grau3 = image[:,400:450]
weiß = image[:,550:600]

print(weiß)