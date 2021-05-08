import cv2
import numpy as np

imagedb = cv2.imread("../../BilderV2/dunkelbild.png")
imagedb = imagedb.astype('float32')

imageub = cv2.imread("../../BilderV2/unbearbeitet.png")
imageub = imageub.astype('float32')

fin = np.subtract(imageub,imagedb)
cv2.imwrite("../BilderV2/dunkelbearbeitet.png", fin.astype('uint8'))
