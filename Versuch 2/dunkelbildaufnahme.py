import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

#Tutorial
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
durchlauf = 0
dunkelbilder = []
tempmean = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        cv2.imwrite("../BilderV2/dunkel" + str(durchlauf) + ".png", gray)
        dunkelbilder.append(cv2.imread("../BilderV2/dunkel" + str(durchlauf) + ".png"))
        durchlauf = durchlauf + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
    if durchlauf == 10:
        dub = np.mean(dunkelbilder, axis=0)
        break;

print(dub)
plt.imshow(dub/255)
plt.show()
cv2.imwrite("../BilderV2/dunkelbild.png", dub)
cap.release()
cv2.destroyAllWindows()