# Das Abtasttheorem besagt, dass ein kontinuierliches, bandbegrenztes Signal,
# mit einer Minimalfrequenz von 0 Hz und einer Maximalfrequenz fmax, mit einer Frequenz
# größer als 2 · fmax abgetastet werden muss, damit man aus dem so erhaltenen zeitdiskreten
# Signal das Ursprungssignal ohne Informationsverlust exakt rekonstruieren und beliebig genau
# approximieren kann.

gemesseneAbtastfrequenz = 8021
nyquistfrequenz = gemesseneAbtastfrequenz / 2

print("Die Nyquistfrequenz ist die Hälfte der Abtastfrequenz")
print("Abtastfrequenz: %f, Nyquistfrequenz: %d" % (gemesseneAbtastfrequenz, nyquistfrequenz))
print("Halbe Nyquistfrequenz: %d" % (nyquistfrequenz/2))
print("Doppelte Nyquistfrequenz: %d" % (nyquistfrequenz*2 - 0.99))


#Messaufgaben:
#• Wählen Sie ein Abtastfrequenz im Intervall [6000, 8000] aus. Lesen Sie in Python mit dem
#entsprechenden RedLab-Befehl die tatsächliche Abtastfrequenz des AD-Wandlers
# für Ihre gewählte Abtastfrequenz aus. Was ist hier also die Nyquist-Frequenz?

#• Angefangen von der halben Nyquist-Frequenz bis zur doppelten Nyquist-Frequenz, variieren
#Sie die Frequenz des Sinusgenerators in 7 Schritten und plotten die entsprechenden Kurven in
#Python für das Protokoll. Diskutieren Sie Ihre Ergebnisse.

#Interpretation
# "Das Abtasttheorem besagt, dass ein kontinuierliches, bandbegrenztes Signal,
# mit einer Minimalfrequenz von 0 Hz und einer Maximalfrequenz fmax, mit einer Frequenz
# größer als 2 · fmax abgetastet werden muss, damit man aus dem so erhaltenen zeitdiskreten
# Signal das Ursprungssignal ohne Informationsverlust exakt rekonstruieren und beliebig genau
# approximieren kann."


    #Die Erhöhnung der Frequenzanzahl sowie die sichtbare Überlappung sind auf das Abtasttheorem
	#zurückzuführen. Dieses besagt, das die Abtastfrequenz immer mindestens das doppelte
	#der Bandbreite/Grundfrequenz betragen muss, bzw. die Nyquistfrequenz, mindestens
	#dieser entspricht. Die Abtastfrequenz des AD-Wandlers beträgt 1000Hz die Nyquistfrequenz
	#also 500Hz.
	#Dies bedeutet, das die ersten drei Frequenzen (250,375, 500) ohne Verlust dargestellt werden
	#können. Da jedoch die Abbildungen von den Frequenzen 625, 750, 875 und 1000 darüber
	#liegen, kommt es hier zu Aliasing, es entstehen also Überlappungen. Dies bedeutet, dass das
	#kontinuierliche Sinussignal nicht mehr fehlerfrei aus dem abgetasteten Signal rekonstruiert
	#werden kann.