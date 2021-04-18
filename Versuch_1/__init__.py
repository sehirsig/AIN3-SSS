import glob

import matplotlib
import matplotlib.pyplot as plt
from numpy import *
from pylab import *
import os


#AUFGABE 1

wertenichtflip = np.array([[69, 375.4],
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

werte = np.flip(wertenichtflip)

#matplotlib.rcParams.update({'font.size': 18, 'text.usetex': True})
#reset: matplotlib.rcParams.update({'font.size': 12, 'font.family': 'sans', 'text.usetex': False})

#fig, axes = plt.subplots(1, 2, figsize=(10,3))

#fig, ax = plt.subplots()

#ax.plot(werte[:,0], werte[:,1])
#ax.set_xlabel('Abstand [in cm]')
#ax.set_ylabel('Spannung [in mV]')
#ax.set_title('Kennlinien');
#show()

m1_data_time = np.genfromtxt('../messwerte/m1.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(3))

m1_data = np.genfromtxt('../messwerte/m1.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m2_data = np.genfromtxt('../messwerte/m2.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m3_data = np.genfromtxt('../messwerte/m3.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m4_data = np.genfromtxt('../messwerte/m4.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m5_data = np.genfromtxt('../messwerte/m5.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m6_data = np.genfromtxt('../messwerte/m6.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m7_data = np.genfromtxt('../messwerte/m7.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m8_data = np.genfromtxt('../messwerte/m8.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m9_data = np.genfromtxt('../messwerte/m9.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m10_data = np.genfromtxt('../messwerte/m10.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m11_data = np.genfromtxt('../messwerte/m11.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m12_data = np.genfromtxt('../messwerte/m12.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m13_data = np.genfromtxt('../messwerte/m13.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m14_data = np.genfromtxt('../messwerte/m14.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m15_data = np.genfromtxt('../messwerte/m15.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m16_data = np.genfromtxt('../messwerte/m16.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m17_data = np.genfromtxt('../messwerte/m17.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m18_data = np.genfromtxt('../messwerte/m18.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m19_data = np.genfromtxt('../messwerte/m19.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
m20_data = np.genfromtxt('../messwerte/m20.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))

data_list = [m1_data, m2_data, m3_data, m4_data, m5_data, m6_data, m7_data,
             m8_data, m9_data, m10_data, m11_data, m12_data, m13_data, m14_data,
             m15_data, m16_data, m17_data, m18_data, m19_data, m20_data]

file_mean = open("mean_data.txt", "w+")
file_std = open("std_data.txt", "w+")
print("start saving Data ...")
count = 0;

data_means = []
messdistanz = [100, 130, 160, 190, 220, 250, 280, 310, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660]

for i in data_list:
    loc_data_mean = np.mean(i, dtype=float)
    loc_data_std = np.std(i, dtype=float)
    count = count + 1
    file_mean.write("%d: Mean: %1.5f |" % (count, loc_data_mean))
    file_mean.write(" STD: %f\n" % loc_data_std)
    data_means.append(loc_data_mean)

print("Data saved")
#for file_name in glob.glob("../messwerte/*csv"):
#    m_data = m1_data_time = np.genfromtxt(file_name, dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
#    loc_data_mean = np.mean(m_data, dtype=float)
#    loc_data_std = np.std(m_data, dtype=float)
#    count = count + 1
#    file_mean.write("%d: Mean: %1.5f |" % (count, loc_data_mean))
#    file_mean.write(" STD: %f\n" % loc_data_std)

#plot
fig, ax = plt.subplots()

ax.plot(messdistanz[:], data_means[:])
ax.set_xlabel('Abstand [in mm]')
ax.set_ylabel('Spannung [in mV]')
ax.set_title('Kennlinien');
show()

# Aufgabe 2.
# Nummer 1 Logarithmieren
logawerteEingang = np.log(werte[:,0])
logawerteAusgang = np.log(werte[:,1])

# Nummer 2 Neue Kennlinie
logawerte = np.log(werte)

#plot
fig, ax = plt.subplots()

ax.plot(logawerte[:,0], logawerte[:,1])
ax.set_xlabel('Abstand [in cm]')
ax.set_ylabel('Spannung [in mV]')
ax.set_title('Kennlinie');
show()

#Nummer 3

#Line re, wert a und b für => y' = a * x' + b
#y = e^b * x^a

x = logawerte[:,0]
y = logawerte[:,1]

(a, b) = np.polyfit(x, y, 1)

#wert a und b für => y' = a * x' + b
#y = e^b * x^a

yp = np.polyval([a, b], x)

#plot
fig, ax = plt.subplots()

ax.plot(x, yp)
ax.grid(True)
ax.scatter(x,y)
ax.set_xlabel('Log Abstand [in cm]')
ax.set_ylabel('Log Spannung [in mV]')
ax.set_title("Log Kennlinie")
show()

#Ergebnis
print("Nichtlineare Kennlinie: y = e^%.3f * x^%.3f" % (a, b))

newY = pow(e, b) * pow(werte[:,0], a)
print(newY)


#Aufgabe 3
