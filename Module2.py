import csv
import psycopg2
import time
from datetime import date

conn = psycopg2.connect(database='Stationszuil', user='postgres', password='Brett.ross15',
                            host='localhost', port='5432')

f = open('berichten.csv', 'r+')
read = f.readlines()
bericht1 = (read[0])
print(bericht1)

f = open('berichten.csv', 'r+')
read = f.readlines()
bericht2 = (read[1])
print(bericht2)

f = open('berichten.csv', 'r+')
read = f.readlines()
bericht3 = (read[2])
print(bericht3)


f = open('berichten.csv', 'r+')
read = f.readlines()
bericht4 = (read[3])
print(bericht4)


f = open('berichten.csv', 'r+')
read = f.readlines()
bericht5 = (read[4])
print(bericht5)

def allereviews():
    with open('berichten.csv', 'r+') as a:
        reader = csv.reader(a)
        reviews = list(reader)


        with conn.cursor() as con:
            for review in reviews:
                con.execute(
                     "INSERT INTO review (bericht, naam, station, datum, tijd) "
                     "VALUES (%s, %s, %s, %s, %s)", review
                )
            conn.commit()
    print('Alle reviews zijn overgezet naar de database.')

allereviews()

def moderator():
    moderator_email = input('Moderator, wat is je email: ')
    moderator_naam = input('Moderator, wat is je naam: ')
    with conn.cursor() as con:
        con.execute("INSERT INTO moderator (email, naam) "
                    "VALUES (%s, %s);", [moderator_email, moderator_naam])
        conn.commit()
    print('Dankjewel!')

moderator()

def reviews1():
    review_tijd = time.strftime('%H:%M:%S')
    review_datum = date.today()
    print(bericht1)
    review_reviewid = '1'
    review_review = input('Goedkeuren of afkeuren: ')
    with conn.cursor() as con:
        con.execute("INSERT INTO beoordeling (reviewid, review, datum, tijd) "
                    "VALUES (%s, %s, %s, %s);",[review_reviewid, review_review, review_datum, review_tijd])
        conn.commit()
    print('Dankjewel voor het beoordelen!')

reviews1()

def reviews2():
    review_tijd = time.strftime('%H:%M:%S')
    review_datum = date.today()
    print(bericht2)
    review_reviewid = '2'
    review_review = input('Goedkeuren of afkeuren: ')
    with conn.cursor() as con:
        con.execute("INSERT INTO beoordeling (reviewid, review, datum, tijd) "
                    "VALUES (%s, %s, %s, %s);",[review_reviewid, review_review, review_datum, review_tijd])
        conn.commit()
    print('Dankjewel voor het beoordelen!')

reviews2()

def reviews3():
    review_tijd = time.strftime('%H:%M:%S')
    review_datum = date.today()
    print(bericht3)
    review_reviewid = '3'
    review_review = input('Goedkeuren of afkeuren: ')
    with conn.cursor() as con:
        con.execute("INSERT INTO beoordeling (reviewid, review, datum, tijd) "
                    "VALUES (%s, %s, %s, %s);",[review_reviewid, review_review, review_datum, review_tijd])
        conn.commit()
    print('Dankjewel voor het beoordelen!')

reviews3()

def reviews4():
    review_tijd = time.strftime('%H:%M:%S')
    review_datum = date.today()
    print(bericht4)
    review_reviewid = '4'
    review_review = input('Goedkeuren of afkeuren: ')
    with conn.cursor() as con:
        con.execute("INSERT INTO beoordeling (reviewid, review, datum, tijd) "
                    "VALUES (%s, %s, %s, %s);",[review_reviewid, review_review, review_datum, review_tijd])
        conn.commit()
    print('Dankjewel voor het beoordelen!')

reviews4()

def reviews5():
    review_tijd = time.strftime('%H:%M:%S')
    review_datum = date.today()
    print(bericht5)
    review_reviewid = '5'
    review_review = input('Goedkeuren of afkeuren: ')
    with conn.cursor() as con:
        con.execute("INSERT INTO beoordeling (reviewid, review, datum, tijd) "
                    "VALUES (%s, %s, %s, %s);",[review_reviewid, review_review, review_datum, review_tijd])
        conn.commit()
    print('Dankjewel voor het beoordelen!')

reviews5()