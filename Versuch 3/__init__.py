import numpy as np

import matplotlib.pyplot as plt

csv_file = "../SoundV3/sound_data.csv"
datamicro = np.genfromtxt(csv_file, dtype = int,usecols=(0))
datamilli = datamicro / 1000
data = datamilli / 1000 #Volt


fouriertransformierte = np.fft.fft(data)

fig, ax = plt.subplots()
ax.set_xlabel('Abtastpunkte')
ax.set_title("Amplitude mit Abtastpunkten")
fig.text(0.02,0.5,'Amplitude (MilliVolt)', ha='center', va='center', rotation='vertical')
ax.plot(datamilli)

plt.show()

M = 225280 #(Anzahl Abtastungen) / Abtastpunkte / Signallänge
aufnehmsekunden = 5.108390023 #(s)
aufnehmmilisekunden = aufnehmsekunden * 1000 #(5108.390023 ms)
deltaT = aufnehmsekunden / M #(0.022675736962890623 ms) Abtastintervall

zeitproabtast = []
for k in range(M):
    zeitproabtast.append(k*deltaT/1000) #ms
fig4, ax4 = plt.subplots()
ax4.set_xlabel('Zeit in Sekunden')
fig4.text(0.02,0.5,'Amplitude (MilliVolt)', ha='center', va='center', rotation='vertical')
ax4.plot(zeitproabtast, datamilli)
ax4.set_title("Amplitude mit Aufnahme-Zeit")
plt.show()



zeittest = []
for t in range(300):
    zeittest.append(t*deltaT)
fig3, ax3 = plt.subplots()
ax3.set_xlabel('Zeit in Millisekunden')
#ax3.set_ylabel('Amplitude')
fig3.text(0.02,0.5,'Amplitude (MilliVolt)', ha='center', va='center', rotation='vertical')
ax3.plot(zeittest, datamilli[0:300])
ax3.set_title("Ausschnitt Grundperiode")
ax3.grid()
plt.show()

#GrundPeriode ausrechnen aus Plot:
# Periode Werte [41.0, 125.0, 209.0, 293.0] * deltaT
# -> Umgerechnet Wert 1: 0.000930, Wert 2: 0.002834, Wert 3: 0.004739, Wert 4: 0.006644:
# Wert 2 - 1: 0.001904 . Wert 3 - 2: 0.001905  Wert 4 - 3: 0.0019049999999999996
# Mittelwert -> 0.001905 Periodendauer (Grundperiode)

#Aufgabe 1
# Grundperiode: 1.905 miliSekunden
# Grundfrequenz: 1/0.001905 => 524.9343832 Hz
# Signaldauer M: 5.108390023 Sekunden
# Abtastfrequenz: 44100 Hz
# Signallänge (Anzahl Abtastungen): 225280
# Abtastintervall deltaT: 0.000022675736962890624 Sekunden
#


frequencys = []
for i in range(len(fouriertransformierte)):
    frequencys.append(i / aufnehmsekunden)

# n / M * deltaT

fig2, ax2 = plt.subplots()
ax2.plot(frequencys, np.abs(fouriertransformierte))
ax2.set_xlabel('Frequenz (Hz)')
ax2.set_ylabel('Amplitude (V)')
ax2.set_title("Amplitudenspektrum")
plt.show()