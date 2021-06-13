import numpy as np

import matplotlib.pyplot as plt

#Aufgabe1 c)

csv_file = "../../SoundV4/sound_data_6942018.csv"
data = np.genfromtxt(csv_file, dtype = int,usecols=(0))

fouriertransformierte = np.fft.fft(data)
aufnehmsekunden = 1 #1 Sekunde

frequencys = []
for i in range(len(fouriertransformierte)):
    frequencys.append(i / aufnehmsekunden)

# n / M * deltaT

fig2, ax2 = plt.subplots()
ax2.plot(frequencys[0:22050], np.abs(fouriertransformierte[0:22050]))
ax2.set_xlabel('Frequenz (Hz)')
ax2.set_ylabel('Amplitude')
ax2.set_title("Amplitudenspektrum")
plt.show()