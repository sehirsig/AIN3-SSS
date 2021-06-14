import scipy.signal as sgl
import numpy as np
import matplotlib.pyplot as plt

#Aufgabe1 d)

csv_file = "../../SoundV4/sound_data_6942018.csv"
data = np.genfromtxt(csv_file, dtype = int,usecols=(0))

# Signal in Abschnitte von 512 Samples

def zerteilen(array):
    gauss_fenster = np.array(sgl.gaussian(512, 512 / 4))
    for i in range(0, len(array) - 512 + 1, 256):
        yield np.concatenate([[0] * i, list(gauss_fenster * array[i:i + 512]), [0] * (len(array) - (i + 512))])

def windowing(array):
    fenster = np.array(list(zerteilen(data)))
    return np.fft.fft(fenster).mean(0)

data_transformed = windowing(data)

fouriertransformierte = np.fft.fft(data)
aufnehmsekunden = 1 #1 Sekunde

frequencys = []
for i in range(len(fouriertransformierte)):
    frequencys.append(i / aufnehmsekunden)

fig2, ax2 = plt.subplots()
ax2.plot(frequencys, np.abs(data_transformed))
ax2.set_xlabel('Frequenz (Hz)')
ax2.set_ylabel('Amplitude')
ax2.set_title("Amplitudenspektrum2")
plt.show()