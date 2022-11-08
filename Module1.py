import csv
import random
import time
from datetime import date

"""
In deze module vraagt het programma de reizigers om hun naam en een bericht.
De reizigers kunnen in dit bericht achter laten wat ze van het station vinden.
Het station word willekeurig gekozen door een programma hieronder.
Daarna word er tijd toegevoegt en word alles in een csv bestand gezet.
"""

#functie voor bericht
def bericht():
    bericht = input('Voer Uw bericht in: ')  #Invoer bericht
    if len(bericht) > 140:  #Kijken of bericht niet langer is dan 140 tekens
        print('Uw bericht mag niet meer dan 140 tekens bevatten.')
    elif len(bericht) <= 0:  #kijken of bericht niet korter is dan 0 tekens
        print('U bent vergeten een bericht achter te laten.')
    else:
        print('Dankje voor Uw bericht.\n')
    return bericht  #Returned het bericht

#Functie voor de naam van de reizger
def naam():
    naam = input('Uw naam: ')  #Invoer naam
    if len(naam) == 0:  #kijken of de naam 0 tekens heeft
        naam = 'Anoniem'  #Als de naam 0 tekens heeft word de naam anoniem
    return naam

#Functie voor het station
def station():
    stations = ['Arnhem', 'Almere', 'Amersfoort', 'Almelo', 'Alkmaar', 'Apeldoorn', 'Assen', 'Amsterdam',
                'Boxtel', 'Breda', 'Dordrecht', 'Delft', 'Deventer', 'Enschede', 'Gouda', 'Groningen',
                'Den Haag', 'Hengelo', 'Haarlem', 'Helmond', 'Hoorn', 'Heerlen', 'Den Bosch', 'Hilversum', 'Leiden',
                'Lelystad', 'Leeuwarden', 'Maastricht', 'Nijmegen', 'Oss', 'Roermond', 'Roosendaal', 'Sittard',
                'Tilburg',
                'Utrecht', 'Venlo', 'Vlissingen', 'Zaandam', 'Zwolle', 'Zutphen']
    randomstation = random.choice(stations)  #Kiest een random station uit de lijst hierboven
    return randomstation

tijd = time.strftime('%H:%M:%S')  #Noteerd de tijd in uur, minuten, seconden
datum = date.today()  #Noteerd de datum jaar, maand, dag

volledigbericht = f'{bericht()}, {naam()}, {station()}, {datum}, {tijd}\n'  #Maakt van alles een compleet bericht


f = open('berichten.csv', 'a+')  #opent het bestand berichten.csv
f.write(volledigbericht)  #Schijft het complete bericht in het geopende bestand
