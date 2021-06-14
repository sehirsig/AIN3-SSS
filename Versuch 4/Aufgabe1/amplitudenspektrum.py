import numpy as np

import matplotlib.pyplot as plt

#Aufgabe1 c)

csv_file = "../../SoundV4/testsound.csv"
data = np.genfromtxt(csv_file, dtype = int,usecols=(0))

fouriertransformierte = np.fft.fft(data)
aufnehmsekunden = 1 #1 Sekunde

print("da: %s" % np.max(fouriertransformierte))

frequencys = []
for i in range(len(fouriertransformierte)):
    frequencys.append(i / aufnehmsekunden)


fig2, ax2 = plt.subplots()
ax2.plot(frequencys, np.abs(fouriertransformierte))
ax2.set_xlabel('Frequenz (Hz)')
ax2.set_ylabel('Amplitude')
ax2.set_title("Amplitudenspektrum")
plt.show()