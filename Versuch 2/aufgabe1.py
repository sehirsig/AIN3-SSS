import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("../BilderV2/unbearbeitet.png")
image = image.astype('float32')

plt.imshow(image)
plt.show()
plt.imshow(image/255)
plt.show()



schwarz = image[:,0:50]
grau1 = image[:,150:200]
grau2 = image[:,300:350]
grau3 = image[:,400:450]
weiß = image[:,550:600]

plt.imshow(schwarz/255)
plt.show()
plt.imshow(grau1/255)
plt.show()
plt.imshow(grau2/255)
plt.show()
plt.imshow(grau3/255)
plt.show()
plt.imshow(weiß/255)
plt.show()

print("Schwarz: STD: %f | Mean: %f" %(np.std(schwarz),np.mean(schwarz)))
print("Grau1: STD: %f | Mean: %f" %(np.std(grau1),np.mean(grau1)))
print("Grau2: STD: %f | Mean: %f" %(np.std(grau2),np.mean(grau2)))
print("Grau3: STD: %f | Mean: %f" %(np.std(grau3),np.mean(grau3)))
print("Weiß: STD: %f | Mean: %f" %(np.std(weiß),np.mean(weiß)))