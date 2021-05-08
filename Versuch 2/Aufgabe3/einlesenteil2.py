import cv2
import numpy as np

imagedb = cv2.imread("../../BilderV2/dunkelbild.png")
imagedb = imagedb.astype('float32')

imagewb = cv2.imread("../../BilderV2/weißbild.png")
imagewb = imagewb.astype('float32')

imageub = cv2.imread("../../BilderV2/unbearbeitet.png")
imageub = imageub.astype('float32')

darksubtract = np.subtract(imageub,imagedb)

meanwhite = np.norm

fin = np.divide(darksubtract, meanwhite)



cv2.imwrite("../BilderV2/aufgabe3bearbeitet.png", fin.astype('uint8'))

