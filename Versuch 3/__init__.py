import numpy as np

import matplotlib.pyplot as plt

csv_file = "../SoundV3/sound_data.csv"
data = np.genfromtxt(csv_file, dtype = int,usecols=(0))


fouriertransformierte = np.fft.fft(data)

fig, ax = plt.subplots()
ax.set_xlabel('Abtastpunkte')
ax.set_ylabel('Frequenz (Hz)')
ax.plot(data)
fig2, ax2 = plt.subplots()
ax2.plot(fouriertransformierte)
plt.show()

#Grundperiode:
#Grundfrequenz:
#Abtastpunkte: 225280
#Abtastintervall:
#

# frequenz = n schwingungen / (Signallänge M) * Abtastintervall
