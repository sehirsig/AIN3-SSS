import numpy as np
import scipy.signal as sgl
import matplotlib.pyplot as plt

def zerteilen(array):
    gauss_fenster = np.array(sgl.gaussian(512, 512 / 4))
    for i in range(0, len(array) - 512 + 1, 256):
        yield np.concatenate([[0] * i, list(gauss_fenster * array[i:i + 512]), [0] * (len(array) - (i + 512))])

def windowing_func(array):
    fenster = np.array(list(zerteilen(array)))
    return np.fft.fft(fenster).mean(0)

#Versuch 2 a)
csv_filedest = "../../SoundV4/"
csv_filename = "hoch/sound_data_hoch"
csv_fileend = ".csv"

alle_spektren = []
for i in range(5):
    data = np.genfromtxt(csv_filedest + csv_filename + str(i + 1) + csv_fileend, dtype = float,usecols=(0))
    alle_spektren.append(windowing_func(data))

Spektrum_Final = np.mean(alle_spektren, 0)

print
csv_file_final = csv_filedest + csv_filename + csv_fileend
np.savetxt(csv_file_final, np.real(Spektrum_Final), delimiter=",")

fouriertransformierte = np.fft.fft(Spektrum_Final)
aufnehmsekunden = 1 #1 Sekunde

frequencys = []
for i in range(len(fouriertransformierte)):
    frequencys.append(i / aufnehmsekunden)


fig2, ax2 = plt.subplots()
ax2.plot(frequencys, np.abs(Spektrum_Final))
ax2.set_xlabel('Frequenz (Hz)')
ax2.set_ylabel('Amplitude')
ax2.set_title("Amplitudenspektrum " + csv_filename)
plt.show()