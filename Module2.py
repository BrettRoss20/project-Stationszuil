import csv
import psycopg2
import time
from datetime import date

conn = psycopg2.connect(database='Stationszuil', user='postgres', password='Brett.ross15',
                            host='localhost', port='5432')


def review():
    moderator_email = input('Moderator, wat is je email: ')
    moderator_naam = input('Moderator, wat is je naam: ')
    with conn.cursor() as con:
        con.execute("INSERT INTO moderator (email, naam) "
                    "VALUES (%s, %s);", [moderator_email, moderator_naam])
        conn.commit()
    print('Dankjewel!')

    while True:
        f = open("berichten.csv", "r+")
        comment = f.readline()
        if comment == '':
            print('Er zijn op dit moment geen berichten om te beoordelen.')
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
        beoordeling = input('Goedkeuren of afkeuren: ')
        review_tijd = time.strftime('%H:%M:%S')
        review_datum = date.today()
        with conn.cursor() as con:
            con.execute("INSERT INTO review (beoordeling, bericht, naam, station, datumbericht, tijdbericht, beoordelingsdatum, beoordelingstijd) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", [beoordeling, bericht, naam, station, datumbericht, tijdbericht, review_datum, review_tijd])
            conn.commit()
        with open(r"berichten.csv", 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[1:])
    print('Dankjewel voor het beoordelen!')

review()