import cv2
import numpy as np

imagedb = cv2.imread("../../BilderV2/dunkelbild.png") #dunkelbild
imagedb = imagedb.astype('float32')

imagewb = cv2.imread("../../BilderV2/weißbild.png") #weißbild
imagewb = imagewb.astype('float32')

imageub = cv2.imread("../../BilderV2/unbearbeitet.png") #unbearbeitetes einlesebild
imageub = imageub.astype('float32')

darksubtract = np.subtract(imageub,imagedb) # Dunkelbild von Eingangsbild abziehen

cv2.imwrite("../BilderV2/dunkelbearbeitet.png", darksubtract.astype('uint8'))

meanwhite = np.divide(imagewb, np.mean(imagewb)) # Weißbild normiert mit Mittelwert zu 1

fin = np.divide(darksubtract, meanwhite) # Bearbeitetes Eingangsbild mit meanwhite dividieren

cv2.imwrite("../BilderV2/aufgabe3bearbeitet.png", fin.astype('uint8'))

