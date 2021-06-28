import math
import numpy as np

# Versuch 3
print("\nVERSUCH 3\n")
# 10-Bit DA-Wandler
uMax10Bit = 5
uMin10Bit = 0
genauigkeit10Bit = ((1)/(np.power(2,10)))
deltaU10Bit = ((uMax10Bit - uMin10Bit)/(np.power(2,10)))
print("Genauigkeit des 10-Bit DA-Wandlers: %f" % genauigkeit10Bit)
print("Theoretischer Quantisierungsfehler des 10-Bit DA-Wandlers: %f V" % deltaU10Bit)
print()

volteingabe = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
oszilloskop = [0.560, 1.033, 1.519, 2.06, 2.534, 3.02, 3.562, 4.037, 4.524, 5.057]

abweichungADV3 = 0

difANV3 = np.subtract(oszilloskop,volteingabe)
print("ref\t\tADV3\tADV3dif")
for i in np.arange(0,10):
    ref = volteingabe[i]
    adV3 = oszilloskop[i]
    adV3DIF = abs(difANV3[i])
    adV3SUM = np.power(adV3DIF,2)
    print("%.4f\t%.4f\t%.4f" % (ref, adV3, adV3DIF))

abweichungADV3 = math.sqrt((1/(len(oszilloskop) - 1)) * adV3SUM)

print("\nStandardabweichung DA-Wandler V3 Oszilloskop: %f" % abweichungADV3)