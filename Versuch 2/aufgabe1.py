import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("../BilderV2/unbearbeitet.png")
image = image.astype('float32')

schwarz = image[:,0:50]
grau1 = image[:,150:200]
grau2 = image[:,300:350]
grau3 = image[:,400:450]
weiß = image[:,550:600]

cv2.imwrite("../BilderV2/unterbildschwarz.png", schwarz.astype('uint8'))
cv2.imwrite("../BilderV2/unterbildgrau1.png", grau1.astype('uint8'))
cv2.imwrite("../BilderV2/unterbildgrau2.png", grau2.astype('uint8'))
cv2.imwrite("../BilderV2/unterbildgrau3.png", grau3.astype('uint8'))
cv2.imwrite("../BilderV2/unterbildweiß.png", weiß.astype('uint8'))

print("Schwarz: STD: %f | Mean: %f" %(np.std(schwarz),np.mean(schwarz)))
print("Grau1: STD: %f | Mean: %f" %(np.std(grau1),np.mean(grau1)))
print("Grau2: STD: %f | Mean: %f" %(np.std(grau2),np.mean(grau2)))
print("Grau3: STD: %f | Mean: %f" %(np.std(grau3),np.mean(grau3)))
print("Weiß: STD: %f | Mean: %f" %(np.std(weiß),np.mean(weiß)))