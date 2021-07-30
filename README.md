# RSAG Telegram BOT
Zeigt Störungsmeldungen von der RSAG über einen Telegram Bot.
Der Bot ist in Python geschrieben.
Der Bot kann momentan gefunden werden unter [@RSAGnewsBOT](https://t.me/RSAGnewsBOT)

## Warnung
Der Bot ist momentan, wegen einer Änderung am lxml-Paket, zerstört.


# Information
Dies ist nur der Source Code
_____________________________________________________________________
# Was bis jetzt schon funktioniert
- Bei dem Command /stoerungen werden alle aktuellen Störungen angezeigt.
- Alle zwei Minuten neuer Scan der Störungswebsite
- Bahn-Emoji bei Tram-Störungen, Bus-Emoji bei Bus-Störungen
- (NEU) Mit /start wird die jeweilige Chat-ID des Benutzers und dessen Vorname in einer von außen unzugänglichen Datenbank gespeichert, damit die folgenden To-Do-Aufgaben demnächst erfüllt werden können.

# To-Do
- Automatisches Senden der Störungsnachricht bei neuer Störung
