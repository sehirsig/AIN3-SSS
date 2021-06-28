import math
import numpy as np

# Versuch 2
print("\nVERSUCH 2\n")
generator = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

boxredlab = [1.09375, 2.08984375, 3.0078125,4.052734, 5.068359, 6.0742187, 7.03125, 8.0371093, 9.0429687, 9.99023437] #AD-Wandler #AD

keithleytrms = [1.040, 2.096, 3.008, 4.065, 5.073, 6.081, 7.043, 8.053, 9.061, 10.071] #Hochgenaues Feinmessgerät #REF

voltcraft = [ 1.035, 2.087, 2.995, 4.05, 5.05, 6.06, 7.02, 8.02, 9.03, 10.03] #Analog #AN Multimeter

# Genauigkeit = ( 1 / 2^n )
# 11-Bit AD-Wandler
uMax11Bit = 10
uMin11Bit = -10
genauigkeit11Bit = ((1)/(np.power(2,11)))
deltaU11Bit = ((uMax11Bit - uMin11Bit)/(np.power(2,11)))
print("Genauigkeit des 11-Bit AD-Wandlers: %f" % genauigkeit11Bit)
print("Theoretischer Quantisierungsfehler des 11-Bit AD-Wandlers: %f V" % deltaU11Bit)
print()
adSUM = 0
anSUM = 0
#ref = keithletrms
difAD = np.subtract(boxredlab,keithleytrms)
difAN = np.subtract(voltcraft,keithleytrms)

print("ref\t\tAD\t\tADdif\tAN\t\tANdif")
for i in np.arange(0,10):
    ref = keithleytrms[i]
    ad = boxredlab[i]
    adDIF = abs(difAD[i])
    adSUM += np.power(adDIF,2)

    analog = voltcraft[i]
    anDIF = abs(difAN[i])
    anSUM += np.power(anDIF,2)

    print("%.4f\t%.4f\t%.4f\t%.4f\t%.4f" % (ref, ad, adDIF, analog, anDIF))

abweichungAD = math.sqrt((1/(len(boxredlab) - 1)) * adSUM)
abweichungAN = math.sqrt((1/(len(voltcraft) - 1)) * anSUM)

print("\nStandardabweichung AD-Wandler BoxRedLab: %f" % abweichungAD)
print("Standardabweichung Analog Voltcraft Multimeter: %f" % abweichungAN)