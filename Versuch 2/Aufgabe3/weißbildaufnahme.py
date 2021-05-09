import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

#Tutorial
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
cap.set(12, cap.get(10)*0.4) #Belichtung 40% der Hellsättigung

durchlauf = 0
weißbilder = []

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        cv2.imwrite("../../BilderV2/weiß" + str(durchlauf) + ".png", gray)
        image = cv2.imread("../../BilderV2/weiß" + str(durchlauf) + ".png")
        weißbilder.append(image.astype('float32'))
        durchlauf = durchlauf + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
    if durchlauf == 10:
        dub = np.mean(weißbilder, axis=0)
        break;

imagedb = cv2.imread("../../BilderV2/dunkelbild.png")
imagedb = imagedb.astype('float32')

fin = np.subtract(dub,imagedb) #Weißbild - Dunkelbild

cv2.imwrite("../../BilderV2/weißbild.png", fin.astype('uint8'))
cap.release()
cv2.destroyAllWindows()