# -*- coding: utf-8 -*-
import os, sys, sqlite3
import lib.functions as func
import logging                      # Zum Loggen
from pathlib import Path            # zum erstellen der Datenbank
import time

# Logger zur Detaillierten Aufzeichnung, in Vorbereitung auf die einfachere Verwendung des GUIs, vielleicht später py2exe um eine einfache exe-Datei für Windows bereit zustellen.
logging.basicConfig(filename="dblog %s.log" %time.time(),
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)





def datenbankErstellen():
    dbname = input("Name der Datenbank: ")
    print("Der Datenbankname wurde festgelegt auf: ",dbname)
    return

def testTable():
    print('Tabellentest wird gestartet.')
    test = 'SELECT * from filme;'
    cursor.execute(test)
    print('Hier der aktuelle Stand der Datenbank')
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2],
          dsatz[3], dsatz[4])
    return



def createTable():
    cursor = connection.cursor() # Zum erstellen von Sachen
    myfile = Path('filme.db')
    myfile.touch(exist_ok=True)
    sql = 'CREATE TABLE filme("id INTEGER PRIMARY KEY, titel TEXT, schauspieler TEXT, laenge INTEGER, regisseur TEXT, bewertung_imdb INTEGER, verfuegbarkeit TEXT, genre TEXT")'
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return


def addMovie():
    cursor = connection.cursor() # Zum erstellen von Sachen
    sql = 'INSERT INTO filme VALUES(01, "Die Verurteilten", "Tim Robbins", 130, "Frank Darabont", 9.6, "Netflix", "Thriller")'
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return




# Als erstes überprüfen, ob eine genannte Datenbank bereits existiert
logger.warning("Versuche Datenbank zu erstellen")
if os.path.exists("filme.db"):
    print("Datei bereits vorhanden")
    logger.warning("Datei konnte nicht erstellt werden, da bereits vorhanden")
else: 
    createTable()

logger.info("Verbinde mit der Datenbank")
connection = sqlite3.connect("filme.db")
logger.info("Erfolg! Verbunden mit der DatenbanK")
print("Verbunden mit der Datenbank")




print("Wilkommen in deiner persönlichen Filmdatenbank.")
print("Folgende Eingaben sind möglich: ")
print("add      -       Hinzufügen eines Films")


print(time.time())
