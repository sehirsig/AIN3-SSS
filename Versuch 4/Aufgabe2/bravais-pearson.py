#Versuch 2 Aufgabe c)

import scipy.stats as scsts
import numpy as np

Spektrum1_rechts = np.genfromtxt("../../SoundV4/sound_data_rechts.csv", dtype = float,usecols=(0))
Spektrum2_tief = np.genfromtxt("../../SoundV4/sound_data_tief.csv", dtype = float,usecols=(0))
Spektrum1_hoch = np.genfromtxt("../../SoundV4/sound_data_hoch.csv", dtype = float,usecols=(0))
Spektrum2_links = np.genfromtxt("../../SoundV4/sound_data_links.csv", dtype = float,usecols=(0))

print("Korrelationen untereinander")
print("Tief - Tief: ", scsts.pearsonr(Spektrum2_tief, Spektrum2_tief)[0])
print("Tief - Hoch: ", scsts.pearsonr(Spektrum2_tief, Spektrum1_hoch)[0])
print("Tief - Rechts: ", scsts.pearsonr(Spektrum2_tief, Spektrum1_rechts)[0])
print("Tief - Links: ", scsts.pearsonr(Spektrum2_tief, Spektrum2_links)[0])