# Das Abtasttheorem besagt, dass ein kontinuierliches, bandbegrenztes Signal,
# mit einer Minimalfrequenz von 0 Hz und einer Maximalfrequenz fmax, mit einer Frequenz
# größer als 2 · fmax abgetastet werden muss, damit man aus dem so erhaltenen zeitdiskreten
# Signal das Ursprungssignal ohne Informationsverlust exakt rekonstruieren und beliebig genau
# approximieren kann.

gemesseneAbtastfrequenz = 8021
nyquistfrequenz = gemesseneAbtastfrequenz / 2
