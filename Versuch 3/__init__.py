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

#Grundperiode: 0,00002267573696145125s (1/44100Hz) ??
#Grundfrequenz: 44100 Hz ??
#Abtastpunkte: 225280
#Abtastintervall: 5,10839ms ??
#

# frequenz = n schwingungen / (Signallänge M) * Abtastintervall
