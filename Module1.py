import csv
import random
import time
from datetime import date

def bericht():
    bericht = input('Voer Uw bericht in: ')
    if len(bericht) > 140:
        print('Uw bericht mag niet meer dan 140 tekens bevatten.')
    elif len(bericht) <= 0:
        print('U bent vergeten een bericht achter te laten.')
    else:
        print('Dankje voor Uw bericht.\n')
    return bericht

def naam():
    naam = input('Uw naam: ')
    if len(naam) == 0:
        naam = 'Anoniem'
    return naam

def station():
    stations = ['Arnhem', 'Almere', 'Amersfoort', 'Almelo', 'Alkmaar', 'Apeldoorn', 'Assen', 'Amsterdam',
                'Boxtel', 'Breda', 'Dordrecht', 'Delft', 'Deventer', 'Enschede', 'Gouda', 'Groningen',
                'Den Haag', 'Hengelo', 'Haarlem', 'Helmond', 'Hoorn', 'Heerlen', 'Den Bosch', 'Hilversum', 'Leiden',
                'Lelystad', 'Leeuwarden', 'Maastricht', 'Nijmegen', 'Oss', 'Roermond', 'Roosendaal', 'Sittard',
                'Tilburg',
                'Utrecht', 'Venlo', 'Vlissingen', 'Zaandam', 'Zwolle', 'Zutphen']
    randomstation = random.choice(stations)
    return randomstation

tijd = time.strftime('%H:%M:%S')
datum = date.today()

volledigbericht = f'{bericht()}, {naam()}, {station()}, {datum}, {tijd}\n'


f = open('berichten.csv', 'a+')
f.write(volledigbericht)

