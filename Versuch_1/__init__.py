import matplotlib
import matplotlib.pyplot as plt
from numpy import *
from pylab import *
#
werte = array([[69, 375.4],
              [66, 379.9],
              [63, 384.4],
              [60, 400.7],
              [57, 416.8],
              [54, 424.1],
              [51, 462.7],
              [48, 484.1],
              [45, 510.4],
              [42, 524.2],
              [39, 563.8],
              [36, 616.9],
              [33, 658.6],
              [30, 697.7],
              [27, 763.8],
              [24, 820.2],
              [21, 896.3],
              [18, 972.5],
              [15, 1075.0],
              [12, 1231.0]])

print(werte)

#matplotlib.rcParams.update({'font.size': 18, 'text.usetex': True})
#reset: matplotlib.rcParams.update({'font.size': 12, 'font.family': 'sans', 'text.usetex': False})
x = linspace(0, 5, 10)


fig, axes = plt.subplots(1, 2, figsize=(10,3))

fig, ax = plt.subplots()

ax.plot(werte[:,0], werte[:,1])
ax.set_xlabel('Abstand [in cm]')
ax.set_ylabel('Spannung [in mV]')
ax.set_title('Kennlinien');
show()