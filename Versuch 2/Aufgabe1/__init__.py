import numpy as np
import imageio
import matplotlib.pyplot as plt
import cv2

#Tutorial
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        cv2.imwrite("../BilderV2/unbearbeitet.png", gray)
        break;
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
print("frame width: " + str(cap.get(3)))
print("frame height: " + str(cap.get(4)))
print("--------------------------------")
print("brightness: " + str(cap.get(10)))
print("contrast: " + str(cap.get(11)))
print("saturation: " + str(cap.get(12)))
print("--------------------------------")
print("gain: " + str(cap.get(14)))
print("exposure: " + str(cap.get(15)))
print("--------------------------------")
print("white balance: " + str(cap.get(17)))
cap.release()
cv2.destroyAllWindows()


#1. Aufnahme und Analyse eines Grauwertkeiles