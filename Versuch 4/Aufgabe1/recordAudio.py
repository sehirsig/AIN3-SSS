import numpy as np
import pyaudio
import numpy
import time
import matplotlib.pyplot as plt

#Aufgabe 1. a) und b)

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 100

p = pyaudio.PyAudio()

print('Sprechen!')
stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,input=True,frames_per_buffer=FRAMESIZE)

data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = numpy.frombuffer(data, np.int16)

stream.stop_stream()
stream.close()
p.terminate()
print('Stop!')

count = 0
start = 0
end = 0
for k in decoded[0:len(decoded)]:
    if k > 500:
        start = count
        print("Start of Audio: " + str(start))
        break
    count += 1

trigger = decoded[start:start + SAMPLEFREQ] # 0 bis SAMPLEFREQ ist 1 Sekunde


randomnumber = np.random.randint(9999999)
plt.plot(decoded)
plt.plot(trigger)
plt.xlabel('Abtastpunkte')
plt.ylabel('Amplitude')
plt.title("yes")
plt.title("Tonaufnahme + Trigger: Sample" + str(randomnumber))
plt.show()

#csv_file = "../../SoundV4/sound_data_" + str(randomnumber) + ".csv"
csv_file = "../../SoundV4/test_sound_data_links.csv"
np.savetxt(csv_file, trigger, delimiter=",")

#data = np.genfromtxt(csv_file, dtype = int,usecols=(0))

