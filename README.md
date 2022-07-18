# Dencrypt
Website für Kontext: https://entenrennen-furtwangen.de/

Dencrypt wurde geschrieben um einfach Tickets zu erstellen, mit unterschiedlichen Nummern und authentifizierungs Codes. Die Codes beinhalteten die symmetrisch verschlüsselte Nummer. Sie wurden mittels eines QR-Codes auf die Rückseite der Tickets gedruckt. Die Software kann erkennen, ob das Ticket gefälscht ist, i.e. ob der Authentifizierungscode falsch ist, ob das Ticket doppelt gescannt wurde oder ob es korrekt ist. Das Entschlüsseln ist darauf ausgelegt, mit einem QR-Code Handscanner durchgeführt zu werden.
Der Code wurde in Python geschrieben. Um den Code ausführen zu können muss man noch eine eigene Datei hinzufügen mit einem zufälligen Salt-Wert, denn man nicht in die Verisonsverwalltung hochladen sollte. Den Code kann man unter https://github.com/NicolasMahn/Dencrypt finden. Der Code steht nicht als Executable (.exe) zur Verfügung.
Verbesserungsvorschläge:
1.	Das Programm sollte die Tickets durchdrucken. Bisher musste man die Tickets nach dem Drucken sortieren, wenn man die Tickets allerdings in der Software richtig sortiert, ist das nichtmehr nötig.

Bisher: 


Besser: 


2.	Einige haben beim Entenrennen versucht ihren QR-Code auf der Rückseite ihres Tickets zu scannen, da ist leider nix passiert. Es wäre vielleicht cool, dass wenn man den QR-Code scannt, man auf die Website kommt und einem der eigene Preis angezeigt wird oder so.
