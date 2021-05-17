import numpy as np

import matplotlib.pyplot as plt

csv_file = "../SoundV3/sound_data.csv"

m1_data = np.genfromtxt(csv_file, dtype = int,usecols=(0))
plt.plot(m1_data)
plt.show()
