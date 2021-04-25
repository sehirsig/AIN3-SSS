import matplotlib.pyplot as plt
from pylab import *

# 1. Ermittlung der Kennlinie des Abstandssensors

#Erstellen Sie eine Python-Funktion, welche die Daten aus der Datei einliest (verwenden Sie
#dazu die Numpy-Funktion genfromtxt()), von den Daten die ersten 1000 Werte überspringt
#und aus den nächsten Werten (nehmen Sie eine sinnvolle Anzahl von Messungen) den
#Mittelwert und die Standardabweichung berechnet (der Einschwingvorgang wird dadurch
#ignoriert). Vergleichen Sie die Ergebnisse mit den Werten aus ihrem Messprotokoll.
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

file_mean = open("mean_data.txt", "w+")
file_std = open("std_data.txt", "w+")
data_list = [m1_data, m2_data, m3_data, m4_data, m5_data, m6_data, m7_data,
             m8_data, m9_data, m10_data, m11_data, m12_data, m13_data, m14_data,
             m15_data, m16_data, m17_data, m18_data, m19_data, m20_data]
data_means = []
data_std = []
messdistanzmm = [100, 130, 160, 190, 220, 250, 280, 310, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660]
messdistanzcm = [10, 13, 16, 19, 22, 25, 28, 31, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66]
count = 0;

for i in data_list:
    loc_data_mean = np.mean(i, dtype=float)
    loc_data_std = np.std(i, dtype=float)
    count = count + 1
    file_mean.write("%d. Mean: %1.5f\n" % (count, loc_data_mean))
    file_std.write("%d. STD: %f\n" % (count, loc_data_std))
    data_means.append(loc_data_mean)
    data_std.append(loc_data_std)


#Stellen Sie die gefundene Übertragungsfunktion bzw. Kennlinie im Protokoll graphisch mit Python
#bzw. Matplotlib dar

fig, ax = plt.subplots()

ax.plot(messdistanzcm[:], data_means[:])
ax.set_xlabel('Abstand [in cm]')
ax.set_ylabel('Spannung [in V]')
ax.set_title('Kennlinien');
show()


#2. Modellierung der Kennlinie durch lineare Regression
#Discord Werte 'a1.pdf'
wertenichtflip = np.array([[69, 0.3754],
              [66, 0.3799],
              [63, 0.3844],
              [60, 0.4007],
              [57, 0.4168],
              [54, 0.4241],
              [51, 0.4627],
              [48, 0.4841],
              [45, 0.5104],
              [42, 0.5242],
              [39, 0.5638],
              [36, 0.6169],
              [33, 0.6586],
              [30, 0.6977],
              [27, 0.7638],
              [24, 0.8202],
              [21, 0.8963],
              [18, 0.9725],
              [15, 1.0750],
              [12, 1.2310]])

werte = np.flip(wertenichtflip) #Flippen, da der Dude ders erstellt hat falsch rum gemessen hat.


#2.1. Logarithmieren Sie zunächst alle (Spannung)Eingangs- und (Entfernung)Ausgangswerte in der Tabelle und
#stellen den Zusammenhang graphisch dar.
werte_x = werte[:,0]
werte_y = werte[:,1]
logawerteEingang = np.log(werte_x) #Spannung Volt
logawerteAusgang = np.log(werte_y) #Abstand cm



#2.2. Der resultierende Kennlinie sollte die Form einer Geraden haben (Plotten)
fig, ax = plt.subplots()

ax.plot(logawerteEingang, logawerteAusgang)
ax.set_xlabel('Log Spannung [in V]')
ax.set_ylabel('Log Abstand [in cm]')
ax.set_title('a1.pdf Kennlinie Logarithmiert');
show()


#2.3. Berechnen Sie mithilfe der linearen Regression, wie in der Vorlesung behandelt, die
#Ausgleichsgerade in Python. Eliminieren Sie ggf. Werte für sehr große Entfernungen,
#für die der lineare Zusammenhang nicht mehr gilt.


#Sie erhalten aus der Regression die Parameter a und b für den Zusammenhang y' = a*x'+b
#Die Rückrechnung auf den ursprünglichen Zusammenhang geschieht über die Umkehrung
#der doppelten Logarithmierung: y = e^b * x^a
#wobei x hier die Spannungsmessung und y die daraus resultierende Abstandsmessung darstellt.
#Damit haben wir die nichtlineare Kennlinie des Sensors gefunden.
x = logawerteEingang
y = logawerteAusgang
(a, b) = np.polyfit(x, y, 1)

yp = np.polyval([a, b], x)

fig, ax = plt.subplots()
ax.plot(x, yp)
ax.grid(True)
ax.scatter(x,y)
ax.set_xlabel('Log Spannung [in V]')
ax.set_ylabel('Log Abstand [in cm]')
ax.set_title("a1.pdf Log Kennlinie")
show()

print("Nichtlineare Kennlinie: y = e^%.3f * x^%.3f" % (b, a))

#3. Flächenmessung mit Fehlerrechnung
#3.a.1
#Stellen Sie das Zielobjekt im Abstand eines DIN-A4-Blattes (lange Seite) vom Sensor auf
#und führen Sie eine einzige Messung aus und speichern Sie das Resultat als csv-Datei
#Länge: 29,7cm -> 697,6 mV
#Breite: 21cm -> 877mV
dina4_breite = np.genfromtxt('../messwerte/dina4b.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))
dina4_laenge = np.genfromtxt('../messwerte/dina4l.csv', dtype = float, delimiter = ',', skip_header = 1017, usecols=(4))

t_6826 = 1.0 # Faktor t bei Sicherheit P = 68,26%
t_95 = 1.96 # Faktor t bei Sicherheit P = 95%

discord_laenge = 0.6796 #V
discord_breite = 0.877 #V

#Kennlinien Formel
def kennlinie(variable_spannung):
  return (pow(e, b) * pow(variable_spannung, a))

#3.a.2
#Schätzen Sie den Messfehler nach der Methode aus der Vorlesung. Vergessen Sie
#dabei nicht eine eventuelle Korrektur aufgrund der Anzahl von Messungen. Geben
#Sie das Ergebnis Ihrer Spannungsmessung in der korrekten Form an. Wie groß ist der
#Vertrauensbereich für eine Sicherheit von 68 %, wie groß für eine Sicherheit von 95 %?
y_meanL = discord_laenge
y_stdL = np.std(dina4_laenge, dtype=float) # Standardabweichung
y_empstdL = (y_stdL / sqrt(dina4_laenge.size)) # Empirische Standardabweichung


print("\n\n")

#3.a.3
#Geben Sie nun das Ergebnis Ihrer Abstandsmessung in cm in korrekter Form an.
#Benutzen sie dazu die Fehlerfortpflanzung.
korrekteAngabe_6826L = (y_meanL + t_6826 * y_empstdL, y_meanL - t_6826 * y_empstdL)
korrekteAngabe_95L = (y_meanL + t_95 * y_empstdL, y_meanL - t_95 * y_empstdL)
print(r" x = %f +- %f * %f [V]" % (y_meanL, t_6826, y_empstdL))
print(r"Messergebnis Laenge mit 68.26%% Sicherheit: %f V bis %f V" % (korrekteAngabe_6826L[0], korrekteAngabe_6826L[1]))
print(r" x = %f +- %f * %f [V]" % (y_meanL, t_95, y_empstdL))
print(r"Messergebnis Laenge mit 95%% Sicherheit: %f V bis %f V" % (korrekteAngabe_95L[0], korrekteAngabe_95L[1]))



#3.b
#Flächenmessung: Zur Ermittlung der Fläche eines DIN A4-Blattes messen Sie nun nach
#derselben Methode wie in Aufgabe 3a die Breite des Blattes aus. Berechnen Sie daraus
#Ihre Schätzung für die Fläche des Blattes und geben Sie Ihr Messergebnis korrekt mit Ihrer
#Schätzung des Messfehlers an. Benutzen Sie dazu das Gaußsche Fehlerfortpflanzungsgesetz
#aus der Vorlesung.

y_meanB = discord_breite
y_stdB = np.std(dina4_breite, dtype=float)
y_empstdB = (y_stdB / sqrt(dina4_breite.size))
print("\n\n")

korrekteAngabe_6826B = (y_meanB + t_6826 * y_empstdB, y_meanB - t_6826 * y_empstdB)
korrekteAngabe_95B = (y_meanB + t_95 * y_empstdB, y_meanB - t_95 * y_empstdB)
print(r" x = %f +- %f * %f [V]" % (y_meanB, t_6826, y_empstdB))
print(r"Messergebnis Breite mit 68.26%% Sicherheit: %f V bis %f V" % (korrekteAngabe_6826B[0], korrekteAngabe_6826B[1]))
print(r" x = %f +- %f * %f [V]" % (y_meanB, t_95, y_empstdB))
print(r"Messergebnis Breite mit 95%% Sicherheit: %f V bis %f V" % (korrekteAngabe_95B[0],korrekteAngabe_95B[1]))

# Fläche = Länge * Breite

#Ableitungsfunktion
def ableitungkennlinie(variable):
  return (a * pow(e, b) * pow(variable, a - 1))

deltaXL = y_empstdL
deltaYL = ableitungkennlinie(discord_laenge) * deltaXL


deltaXB = y_empstdB
deltaYB = ableitungkennlinie(discord_breite) * deltaXB


print("\nLänge: x = %f +- %f [cm]" % (kennlinie(discord_laenge), -deltaYL))
print("Breite: x = %f +- %f [cm]" % (kennlinie(discord_breite), -deltaYB))

eingang1 = kennlinie(discord_laenge)
eingang2 = kennlinie(discord_breite)
# Fläche = eingang1 * eingang2
ableitungeingang1 = eingang2
ableitungeingang2 = eingang1

flaecheV = eingang1 * eingang2
flaecheDeltaV = sqrt(pow(ableitungeingang1 * deltaYL, 2) + pow(ableitungeingang2 * deltaYB, 2))


print("\nFlaeche Max: x = %f +- %f [cm^2]" % (flaecheV, flaecheDeltaV))
