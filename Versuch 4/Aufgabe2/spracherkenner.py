import numpy as np
import scipy.signal as sgl
import scipy.stats as scsts
import matplotlib.pyplot as plt

def zerteilen(array):
    gauss_fenster = np.array(sgl.gaussian(512, 512 / 4))
    for i in range(0, len(array) - 512 + 1, 256):
        yield np.concatenate([[0] * i, list(gauss_fenster * array[i:i + 512]), [0] * (len(array) - (i + 512))])

def windowing_func(array):
    fenster = np.array(list(zerteilen(array)))
    return np.fft.fft(fenster).mean(0)

Spektrum_rechts = np.genfromtxt("../../SoundV4/sound_data_rechts.csv", dtype = float,usecols=(0))
Spektrum_tief = np.genfromtxt("../../SoundV4/sound_data_tief.csv", dtype = float,usecols=(0))
Spektrum_hoch = np.genfromtxt("../../SoundV4/sound_data_hoch.csv", dtype = float,usecols=(0))
Spektrum_links = np.genfromtxt("../../SoundV4/sound_data_links.csv", dtype = float,usecols=(0))

#Hier die File einfügen
inputfile = np.genfromtxt("../../SoundV4/testsound.csv", dtype = float,usecols=(0))
ip = np.abs(windowing_func(inputfile))

woerter = ["Hoch", "Tief", "Rechts", "Links"]
auswertung = 0 # 1 = hoch, 2 = tief, 3 = rechts, 4 = links
ausmax = 0

korr_hoch = scsts.pearsonr(ip, Spektrum_hoch)[0] # [0] für den RealTeil
auswertung = 1
ausmax = korr_hoch
print("Korrelation Hoch: " + str(korr_hoch))
korr_tief = scsts.pearsonr(ip, Spektrum_tief)[0]
if (korr_tief > ausmax):
    auswertung = 2
    ausmax = korr_tief
print("Korrelation Tief: " + str(korr_tief))
korr_rechts = scsts.pearsonr(ip, Spektrum_rechts)[0]
if (korr_rechts > ausmax):
    auswertung = 3
    ausmax = korr_rechts
print("Korrelation Rechts: " + str(korr_rechts))
korr_links = scsts.pearsonr(ip, Spektrum_links)[0]
if (korr_links > ausmax):
    auswertung = 4
    ausmax = korr_links
print("Korrelation links: " + str(korr_links))

print("")
print("Erkanntes Wort: " + woerter[auswertung - 1])
print("Korrelation: " + str(ausmax))