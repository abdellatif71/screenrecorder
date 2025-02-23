Screen Recorder
Dieses Projekt enthält ein Python-Skript, das mithilfe von Tkinter eine grafische Benutzeroberfläche (GUI) für die Bildschirmaufnahme bereitstellt. Mit dem Tool kannst du einen Bereich auf deinem Bildschirm auswählen, die Aufnahme starten und stoppen. Das Video wird als screen_record.avi gespeichert.

Inhaltsverzeichnis
Funktionen
Voraussetzungen
Installation
Verwendung
Problemlösung
Lizenz
Funktionen
Bereichsauswahl: Klicke zweimal auf die Anzeige, um die Koordinaten des aufzunehmenden Bereichs zu speichern.
Aufnahme starten: Nimmt den ausgewählten Bereich in regelmäßigen Abständen auf.
Aufnahme stoppen: Beendet die Aufnahme und speichert das Video als screen_record.avi.
Voraussetzungen
Python 3
Tkinter: Wird standardmäßig mit Python installiert.
Benötigte Python-Pakete:
pyautogui
opencv-python
numpy
Installation
Python installieren:
Stelle sicher, dass Python 3 installiert ist. Lade es von der offiziellen Python-Website herunter, falls noch nicht geschehen.

Virtuelle Umgebung (optional):
Es wird empfohlen, eine virtuelle Umgebung zu verwenden. Erstelle und aktiviere diese wie folgt:

bash
Copier
Modifier
python3 -m venv .venv
source .venv/bin/activate
Abhängigkeiten installieren:
Installiere die benötigten Pakete mit folgendem Befehl:

bash
Copier
Modifier
pip install pyautogui opencv-python numpy
Verwendung
Starte die Anwendung:
Stelle sicher, dass du in der virtuellen Umgebung arbeitest (falls du diese benutzt) und führe das Skript aus:

bash
Copier
Modifier
python screenrecorder.py
Alternativ, wenn du keine virtuelle Umgebung nutzt:

bash
Copier
Modifier
python3 screenrecorder.py
Bereich auswählen:
Klicke zweimal auf das graue Feld, um den aufzunehmenden Bereich auszuwählen. Nach der Auswahl wird eine Meldung mit den Koordinaten angezeigt.

Aufnahme starten:
Klicke auf den Button Start Recording, um die Aufnahme zu beginnen. Es erscheint eine Benachrichtigung, dass die Aufnahme gestartet wurde.

Aufnahme stoppen:
Klicke auf den Button Stop Recording, um die Aufnahme zu beenden und das Video zu speichern.

Problemlösung
Modul nicht gefunden (ModuleNotFoundError):
Stelle sicher, dass du die Pakete in der aktiven virtuellen Umgebung installiert hast oder installiere sie systemweit.

Tkinter-Probleme unter Linux:
Falls Tkinter nicht verfügbar ist, installiere es über:

bash
Copier
Modifier
sudo apt install python3-tk
Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.