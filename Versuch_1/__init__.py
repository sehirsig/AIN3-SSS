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

werte = np.flip(wertenichtflip) #Flippen, da der Dude ders erstellt hat falsch rum gemessen hat.

fig, ax = plt.subplots()
werte_x = werte[:,1]
werte_y = werte[:,0]
#werte[:,1] = x
#werte[:,0] = y
ax.plot(werte_x, werte_y)
ax.set_xlabel('Abstand [in mm]')
ax.set_ylabel('Spannung [in mV]')
ax.set_title('Kennlinien');
show()


#Daten einlesen (Moodle Daten) Hieraus Funktion machen!
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
#Hier kann man (oder drüber) die data_list und messdistanz in eine liste packen, mit zugehörigen tupeln z.b., oder wie oben (ARRAY/ARRAY)
data_means = []
messdistanz = [100, 130, 160, 190, 220, 250, 280, 310, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660]

#plot
for i in data_list:
    loc_data_mean = np.mean(i, dtype=float)
    loc_data_std = np.std(i, dtype=float)
    count = count + 1
    file_mean.write("%d: Mean: %1.5f |" % (count, loc_data_mean))
    file_mean.write(" STD: %f\n" % loc_data_std)
    data_means.append(loc_data_mean)

print("Data saved")
#plot
#fig, ax = plt.subplots()

#ax.plot(messdistanz[:], data_means[:])
#ax.set_xlabel('Abstand [in mm]')
#ax.set_ylabel('Spannung [in mV]')
#ax.set_title('Kennlinien');
#show()

# Aufgabe 2.
# Nummer 1 Logarithmieren
logawerteEingang = np.log(werte_x)
logawerteAusgang = np.log(werte_y)

# Nummer 2 Neue Kennlinie
logawerte = np.log(werte)
print(logawerte)
#plot
fig, ax = plt.subplots()

ax.plot(logawerte[:,1], logawerte[:,0]) # logawerte[:,1] = x, logawerte[:,0] = y
ax.set_xlabel('Abstand [in cm]')
ax.set_ylabel('Spannung [in mV]')
ax.set_title('Kennlinie');
show()


excellogawerteEingang = np.log(messdistanz)
excellogawerteAusgang = np.log(data_means)
excelx = excellogawerteEingang[:]
excely = excellogawerteAusgang[:]
(excela, excelb) = np.polyfit(excelx, excely, 1)
excelyp = np.polyval([excela, excelb], excelx)
print("EXCEL: Nichtlineare Kennlinie: y = e^%.3f * x^%.3f" % (excela, excelb))
#excelnewY = pow(e, excelb) * pow(messdistanz, excela) #Rückrechnung

#Nummer 3

#Line re, wert a und b für => y' = a * x' + b
#y = e^b * x^a

x = logawerte[:,1]
y = logawerte[:,0]

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

#newY = pow(e, b) * pow(werte[:,1], a) #Rückrechnung
#print(newY)


#Aufgabe 3
#Nummer 1
#DIN A4 PDF a1.pdf
#Länge: 29,7cm -> 697,6 mV
#Breite: 21cm -> 877mV
dina4_breite = np.genfromtxt('../messwerte/dina4b.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
dina4_laenge = np.genfromtxt('../messwerte/dina4l.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))

t_6826 = 1.03 # Faktor t bei Sicherheit P = 68,26%
t_95 = 2.09 # Faktor t bei Sicherheit P = 95%

#Nummer 2 BREITE
y_meanB = np.mean(dina4_breite, dtype=float)
y_stdB = np.std(dina4_breite, dtype=float) # Mittelwert EINZELWERT
y_empstdB = (y_stdB / sqrt(dina4_breite.size)) # Mittelwert alle Werte
print("\n\nArithmetisches Mittel Breite Ausgangswerte: %f V" % y_meanB)
print("Empirische Standardabweichung Breite Ausgangswerte: %f V" % y_empstdB)

korrekteAngabe_6826B = (y_meanB + t_6826 * y_empstdB, y_meanB - t_6826 * y_empstdB)
korrekteAngabe_95B = (y_meanB + t_95 * y_empstdB, y_meanB - t_95 * y_empstdB)
print(r"Messergebnis Breite mit 68.26 Sicherheit: %f V bis %f V" % (korrekteAngabe_6826B[1], korrekteAngabe_6826B[0]))
print(r"Messergebnis Breite mit 95 Sicherheit: %f V bis %f V" % (korrekteAngabe_95B[1],korrekteAngabe_95B[0]))

print("\n")
#Nummer 2 LÄNGE
y_meanL = np.mean(dina4_laenge, dtype=float)
y_stdL = np.std(dina4_laenge, dtype=float) # Mittelwert EINZELWERT
y_empstdL = (y_stdL / sqrt(dina4_laenge.size)) # Mittelwert alle Werte
print("Arithmetisches Mittel Laenge Ausgangswerte: %f V" % y_meanL)
print("Empirische Standardabweichung Laenge Ausgangswerte: %f V" % y_empstdL)


korrekteAngabe_6826L = (y_meanL + t_6826 * y_empstdL, y_meanL - t_6826 * y_empstdL)
korrekteAngabe_95L = (y_meanL + t_95 * y_empstdL, y_meanL - t_95 * y_empstdL)
print(r"Messergebnis Laenge mit 68.26 Sicherheit: %f V bis %f V" % (korrekteAngabe_6826L[1], korrekteAngabe_6826L[0]))
print(r"Messergebnis Laenge mit 95 Sicherheit: %f V bis %f V" % (korrekteAngabe_95L[1],korrekteAngabe_95L[0]))

#Nummer 3 Breite
#Fehlerfortpflanzung

discordwert = (pow(e, b) * pow(21, a)) # Kennlinie a1.pdf Discord
deriativeDiscord = 1.81023 * pow(21,2.682) #Wolfram Alpha ausgerchnet #21 ist VARIABLE X EINFACH IRGENDEIN CM / Strecke
#deltaXDISCORD =

#FINALWERT = Discordwert +- deriative * delta x
print("Laenge: %f mV" % discordwert)



excelnewY = (pow(e, excelb) * pow(210, excela)) # Kennline Excel Tabellen Moodle
deriativeMoodle = 4.36322 * pow(21,7.966) #Wolfram Alpha ausgerchnet #21 ist VARIABLE X EINFACH IRGENDEIN CM / Strecke
#deltaXMOODLE =
print("Laenge: %f V" % excelnewY)