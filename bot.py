#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import os
import sys
import asyncio
import re
import time
import random
import datetime
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
import requests
from lxml import html
import threading
import sqlite3

rsag_contents = []
ancor_emoji = '\N{anchor}'
bus_emoji = '\N{bus}'
train_emoji = '\N{tram car}'

def rsag_stoerungen():
    global rsag_contents

    threading.Timer(120.0, rsag_stoerungen).start()

    page_rsag = 'https://www.rsag-online.de/?eID=stoerungsmeldungen'
    page = requests.get(page_rsag, timeout=15)
    npage = re.sub(r'(\r\n|\n|\r)+', ' ', page.text)

    tree = html.fromstring(npage)

    rsag_contents = tree.xpath('//div[@class="col-xs-10 col-sm-10 col-md-8 stoerung-content"]/h3/text()')
    rsag_datums = tree.xpath('//p[@class="datum"]/text()')
    #rsag_grund = tree.xpath('//div[@class="col-xs-10 col-sm-10 col-md-8 stoerung-content"]/h3/text()')

    #for rsag_content, rsag_datum in zip(rsag_contents, rsag_datums):
    #    print (rsag_content, ' '.join(rsag_datum.split()))

    if len(rsag_contents) == 0:
        rsag_contents = ['Zurzeit gibt es keine Störungen! Freie Fahrt, Matrose! ' + ancor_emoji]
    else:
        for i in range(len(rsag_contents)):
            emoji = ''
            linie = re.search(r'\d+', rsag_contents[i][8:])
        if linie:
                if linie.group().isdigit():
                    if int(linie.group()) > 9:
                        emoji = bus_emoji + ' '
                    else:
                        emoji = train_emoji + ' '
                    rsag_contents[i] = emoji + rsag_contents[i]

    for rsag_content in rsag_contents:
        print (rsag_content)

async def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Es ist ein Command gekommen: %s' % command )

    if command  == '/stoerungen':
        for stoerung in rsag_contents:
            await bot.sendMessage(chat_id, stoerung)

    if command  == '/tickets':
        await bot.sendMessage(chat_id, 'Hier findest du alle Infos zu den Tickets\nEinzelfahrkarte - 2.30€\nEinzelfahrkate ermäßigt* - 1.70€\nTageskarte - 6.00€\nTageskarte ermäßigt - 3.90€\nFährfahrkarte - 1.50€\nFährfahrkarte ermäßigt - 1.00€\n\nTickets kannst du dir auch über die RSAG-App holen:\nAndroid: https://goo.gl/ZeKSb8\niOS: https://itunes.apple.com/de/app/rsag-fahrplan/id1380245501?mt=8\n\n*Kinder bis 6 Jahre frei, ermäßigt gilt ab dem 6. bis zum 14.  Lebensjahr\nAlle Angaben ohne Gewähr\niOS is a Trademark of Apple Inc. All rights of this naming are going to Apple.')

    if command  == '/linie1':
        await bot.sendMessage(chat_id, 'Hier findest du alle Infos zur Linie 1.\nDie Linie 1 verkehrt zwischen den Haltestellen Hafenallee-Toitenwinkel und Mecklenburger Allee-Lütten Klein. mit einem anderem command findest du herraus, wann die nächste 1 an deiner Haltestelle fährt. Dazu musst du nur die folgenden Klammern durch deine Haltestelle zusammengeschrieben ersetzen und abschicken.\nBeispiel: /linie1zeitDierkowerKreuz\nDer Command: /linie1zeit(Klammern weg und Haltestelle wie im Beispiel angezeigt einsetzen.)')

    if command  == '/linie1zeit':
        await bot.sendMessage(chat_id, 'Hier sind alle Stationen der Linie 1 als Command:\n/linie1zeitHafenallee\n/linie1zeitFriedensforum\n/linie1zeitMartinNiemoellerStr\n/linie1zeitDierkowerKreuz\n/linie1zeitStadthafen\n/linie1zeitSteintorIHK\n/linie1zeitNeuerMarkt\n/linie1zeitLangeStrasse\n/linie1zeitKroepelinerTor\n/linie1zeitDoberanerPlatz\n/linie1zeitVolkstheater\n/linie1zeitKabutzenhof\n/linie1zeitMassmannstrasse\n/linie1zeitSHolbeinplatz\n/linie1zeitHeinrichSchuetzStr\n/linie1zeitKunsthalle\n/linie1zeitReutershagen\n/linie1zeitSMarienehe\n/linie1zeitEvershagenSued\n/linie1zeitBertholtBrechtStr\n/linie1zeitThomasMorusStr\n/linie1zeitHelsinkierStrasse\n/linie1zeitLuettenKleinZentrum\n/linie1zeitWarnowallee\n/linie1zeitRuegenerStrasse\n/linie1zeitMecklenburgerAllee')

    if command  == '/start':
        connection = rsagbot_connection(database)
        insert_user(connection, (msg['chat']['id'], msg['chat']['first_name']))
        await bot.sendMessage(chat_id, '🤖 BEEP:BEEP\nDas ist der Störungsmelder der RSAG. Der Bot entwickelt sich weiter! Du kannst jetzt alle Störungen der RSAG mit /stoerungen abfragen. ⚓️')

    if command  == '/neu':
        await bot.sendMessage(chat_id, 'Dieser Bot entwickelt sich weiter!\nJETZT NEU IST:\n-Wenn du /start eingibst, wird deine Chat ID in einer bei uns liegenden Datenbank gespeichert, sodass demnächst auch schon neue Meldungen automatisch an jeden geschickt werden, der den Bot gestartet hat. Weitere Infos dazu findest du mit /daten')

    if command  == '/daten':
        await bot.sendMessage(chat_id, 'Mit dem Starten des Bots wird deine Chat ID bestehend aus vielen Zahlen und dein Vorname in einer bei uns stehenden Datenbank gespeichert um später automatisch neue Meldungen an dich zu senden. Diese Datenbank ist nicht von außen zu erreichen und nur auf einem einzigen Gerät gespeichert.')

    if command  == '/news':
        await bot.sendMessage(chat_id, 'Moin! Hier sind die aktuellen News zur RSAG:\n\nVerlängerung der Linie 39 von Reutershagen über Bonhoefferstraße zum Markt Reutershagen weiter über Ostseestadion, Schillingallee, Platz der Jugend und Campus Südstadt bis zum Hauptbahnhof Süd.\nMehr lesen: http://bit.ly/2FOAj1M\n\nDie neue Expressbuslinie X41 - In 20 Minuten von Dierkow nach Lütten Klein - Durch den Tunnel aber ohne Maut zu bezahlen.\nMehr lesen:http://bit.ly/2FLlRrG' )

def rsagbot_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

def rsagbot_db_anlegen(db_file):
    connection = rsagbot_connection(db_file)
    cursor = connection.cursor()
    sql = "CREATE TABLE users(id INTEGER PRIMARY KEY, first_name VARCHAR(30), last_name VARCHAR(30))"
    cursor.execute(sql)
    connection.commit()
    connection.close()

def insert_user(conn, user):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    print(user) 
    sql = ''' INSERT OR IGNORE INTO users(id, first_name)
              VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid



database = r"/home/pi/telepot/txt/rsagbot.db"

if not os.path.exists(database):
    rsagbot_db_anlegen(database)


rsag_stoerungen()

bot = telepot.aio.Bot('**** ADD TOKEN HERE ****')
#bot.message_loop(handle)
loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, handle).run_forever())

print ('Ich höre zu...')

# while 1:
#   time.sleep(10)

loop.run_forever()
