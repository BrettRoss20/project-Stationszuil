import csv
import psycopg2
import time
from datetime import date

conn = psycopg2.connect(database='DatabaseStationszuil', user='postgres', password='Brett.ross15',
                            host='localhost', port='5432')

def review():
    print('Welkom! Vul hier onder je email in.\n')
    f = open('moderators.txt', 'r+')
    read = f.readlines()
    moderator_email = input('Moderator, wat is je email: ')
    if moderator_email in read:
        print('Welkom terug! Je staat al in ons systeem, je kunt gelijk door met het beoordelen van berichten.\n')
    else:
        print('Je staat nog niet in onze database, wat leuk dat je mee wil doen. Vul nogmaals je email in.\n')
        moderator_email = input('Moderator, wat is je email: ')
        moderator_naam = input('Moderator, wat is je naam: ')
        f = open('moderators.txt', 'w')
        f.write(moderator_email)
        with conn.cursor() as con:
            con.execute("INSERT INTO moderator (email, naam) "
                        "VALUES (%s, %s);", [moderator_email, moderator_naam])
            conn.commit()
            print('Dankjewel!')
            print('Succes met het beoordelen van de berichten!\n')

    while True:
        f = open("berichten.csv", "r+")
        comment = f.readline()
        if comment == '':
            print('Er zijn op dit moment geen berichten meer om te beoordelen.')
            conn.close()
            break
        f = open('berichten.csv', 'r+')
        bericht = f.readline()
        berichtgesplit = bericht.split(",")
        bericht = berichtgesplit[0]
        naam = berichtgesplit[1]
        station = berichtgesplit[2]
        datumbericht = berichtgesplit[3]
        tijdbericht = berichtgesplit[4]
        print(bericht, naam, station, datumbericht, tijdbericht)
        beoordeling = input('Vul in afgekeurd of goedgekeurd: ')
        if beoordeling == 'afgekeurd':
            s = open(r"berichten.csv", 'r+')
            lines = s.readlines()
            s.seek(0)
            s.truncate()
            s.writelines(lines[1:])
            break
        else:
            review_tijd = time.strftime('%H:%M:%S')
            review_datum = date.today()
            with conn.cursor() as con:
                con.execute(
                    "INSERT INTO review (beoordeling, bericht, naam, station, datumbericht, tijdbericht, beoordelingsdatum, beoordelingstijd, moderatoremail) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    [beoordeling, bericht, naam, station, datumbericht, tijdbericht, review_datum, review_tijd,
                     moderator_email])
                conn.commit()
            with open(r"berichten.csv", 'r+') as fp:
                lines = fp.readlines()
                fp.seek(0)
                fp.truncate()
                fp.writelines(lines[1:])
    print('Dankjewel voor het beoordelen!')

review()
