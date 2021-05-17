import numpy as np

import matplotlib.pyplot as plt

csv_file = "../SoundV3/sound_data.csv"
data = np.genfromtxt(csv_file, dtype = int,usecols=(0))


fouriertransformierte = np.fft.fft(data)

fig, ax = plt.subplots()
ax.set_xlabel('Abtastpunkte')
ax.set_ylabel('Amplitude')
ax.plot(data)

plt.show()

M = 225280 #(Anzahl Abtastungen) / Abtastpunkte / Signallänge
aufnehmsekunden = 5.108390023 #(s)
aufnehmmilisekunden = aufnehmsekunden * 1000 #(5108.390023 ms)
deltaT = aufnehmsekunden / M #(0.022675736962890623 ms) Abtastintervall

zeitproabtast = []
for k in range(M):
    zeitproabtast.append(k*deltaT)

fig3, ax3 = plt.subplots()
ax3.set_xlabel('Zeit in Sekunden')
ax3.set_ylabel('Amplitude')
ax3.plot(zeitproabtast, data)

plt.show()


#Aufgabe 1
# Grundperiode: ... miliSekunden
# Grundfrequenz: ... Hz
# Signaldauer M : 5.108390023 Sekunden
# Abtastfrequenz: 44100 Hz
# Signallänge M: 225280
# Abtastintervall deltaT: 0.000022675736962890624 Sekunden
#

grundfrequenz = np.min(np.abs(fouriertransformierte))
print(grundfrequenz)
frequencys = []
for i in range(len(fouriertransformierte)):
    frequencys.append(i / aufnehmsekunden)

# n / M * deltaT

fig2, ax2 = plt.subplots()
ax2.plot(frequencys, np.abs(fouriertransformierte))
ax2.set_xlabel('Frequenz (Hz)')
ax2.set_ylabel('Amplitude (V)')
plt.show()