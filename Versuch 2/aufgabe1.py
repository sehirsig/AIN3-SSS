import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

image = imageio.imread("../BilderV2/unbearbeitet.png")
image = image.astype('float32')
plt.imshow(image)
plt.show()

schwarz = np.array(image[:,0:50])
grau1 = np.array(image[:,150:200])
grau2 = np.array(image[:,300:350])
grau3 = np.array(image[:,400:450])
weiß = np.array(image[:,550:600])




print(schwarz.std())
print(schwarz.mean())