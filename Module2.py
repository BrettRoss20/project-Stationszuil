import csv
import psycopg2
import time
from datetime import date

"""
In deze module controleerd de moderator of het geschreven bericht goed is.
De moderator kan het bericht goed of afkeuren.
Als de moderator het goedkeurd word het bericht naar de database in SQL verstuurd.
Als de moderator het bericht afkeurd word het NIET naar de database verstuurd en
word het gelijk verwijdert uit het CSV bestand.
Er word hiervoor een connectie gemaakt met de database.
"""

#Connectie maken met de database
conn = psycopg2.connect(database='DatabaseStationszuil', user='postgres', password='Brett.ross15',
                            host='localhost', port='5432')

#Functie voor de review
def review():
    print('Welkom! Vul hier onder je email in.\n')

    f = open('moderators.txt', 'r+')  #opent het bestand moderators.txt en leest het
    read = f.readlines()
    moderator_email = input('Moderator, wat is je email: ')  #vraagt de moderator om een email
    #kijkt of de moderator al in het bestand staat
    if moderator_email in read:
        print('Welkom terug! Je staat al in ons systeem, je kunt gelijk door met het beoordelen van berichten.\n')
    else:
        print('Je staat nog niet in onze database, wat leuk dat je mee wil doen. Vul nogmaals je email in.\n')
        moderator_email = input('Moderator, wat is je email: ')  #Vraagt de nieuwe moderator om zijn/haar email
        moderator_naam = input('Moderator, wat is je naam: ')  #Vraagt de moderator om zijn naam

        f = open('moderators.txt', 'w')  #Opent het bestand moderators.txt
        f.write(moderator_email)  #schrijft de email
        #Schijft email en naam naar de database
        with conn.cursor() as con:
            con.execute("INSERT INTO moderator (email, naam) "
                        "VALUES (%s, %s);", [moderator_email, moderator_naam])
            conn.commit()
            print('Dankjewel!')
            print('Succes met het beoordelen van de berichten!\n')

    while True:
        f = open("berichten.csv", "r+")  #Opent het bestand berichten.csv
        comment = f.readline()  #Leest het bestand
        if comment == '':  #als er geen comments meer zijn
            print('Er zijn op dit moment geen berichten meer om te beoordelen.')
            conn.close()
            break
        f = open('berichten.csv', 'r+')
        bericht = f.readline()

        berichtgesplit = bericht.split(",")  #Split het bericht in bericht, naam, station, datum, tijd
        bericht = berichtgesplit[0]
        naam = berichtgesplit[1]
        station = berichtgesplit[2]
        datumbericht = berichtgesplit[3]
        tijdbericht = berichtgesplit[4]

        print(bericht, naam, station, datumbericht, tijdbericht)
        beoordeling = input('Vul in afgekeurd of goedgekeurd: ')  #Input van moderator

        if beoordeling == 'afgekeurd':  #als de moderator afgekeurd typt delete hij het bericht in de file berichten.csv
            s = open(r"berichten.csv", 'r+')
            lines = s.readlines()
            s.seek(0)
            s.truncate()
            s.writelines(lines[1:])
            break
        else:
            review_tijd = time.strftime('%H:%M:%S')  #Noemt de tijd in uur, minuten en seconden
            review_datum = date.today()  #Noemt de datum in jaar, maand, dag
            with conn.cursor() as con:  #Insert de beoordeling in de SQL database
                con.execute(
                    "INSERT INTO review (beoordeling, bericht, naam, station, datumbericht, tijdbericht, beoordelingsdatum, beoordelingstijd, moderatoremail) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    [beoordeling, bericht, naam, station, datumbericht, tijdbericht, review_datum, review_tijd,
                     moderator_email])
                conn.commit()
            with open(r"berichten.csv", 'r+') as fp:  #Opent het bestand berichten.csv
                lines = fp.readlines()
                fp.seek(0)
                fp.truncate()
                fp.writelines(lines[1:])  #delete de beoordeelde berichten
    print('Dankjewel voor het beoordelen!')

review()
