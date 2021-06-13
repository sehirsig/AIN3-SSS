import scipy.signal as sgl
import numpy as np
import matplotlib.pyplot as plt
import math

#Aufgabe1 d)

csv_file = "../../SoundV4/sound_data_6942018.csv"
data = np.genfromtxt(csv_file, dtype = int,usecols=(0))


gauss_fenster = np.array(sgl.gaussian(512, 512/4))

# Signal in Abschnitte von 512 Samples


dataabschnitte = []
tempabschnitt = []
for i in data:
    tempabschnitt.append(i)
    if len(tempabschnitt) == 512:
        dataabschnitte.append(tempabschnitt)
        tempabschnitt = tempabschnitt[256:512]
    if (len(tempabschnitt) == 324) & (len(dataabschnitte) == 171):
        dataabschnitte.append(tempabschnitt)
        tempabschnitt = []

#print('%s'% len(dataabschnitte[171]))



windows = []

for k in range(len(dataabschnitte)):
    if k != 171:
        windows.append(np.multiply(dataabschnitte[k], gauss_fenster))
        #bearbeitet.append(np.multiply(dataabschnitte[k], gauss_fenster))
    else:
        windows.append(np.multiply(dataabschnitte[k], gauss_fenster[0:324]))
        #bearbeitet.append(np.multiply(dataabschnitte[k], gauss_fenster[0:324]))

#tdd = np.fft.rfft(windows).mean(0)
print('%s'% windows)





fouriertransformierte = np.fft.fft(data)
aufnehmsekunden = 1 #1 Sekunde



freqs = np.fft.rfftfreq(len(data), 1 / 44100)
limit = np.argmax(freqs > 1000)

#fig2, ax2 = plt.subplots()
#ax2.plot(freqs[1:limit], np.abs(data_fft[1:limit]))
#ax2.set_xlabel('Frequenz (Hz)')
#ax2.set_ylabel('Amplitude')
#ax2.set_title("Amplitudenspektrum")
#plt.show()