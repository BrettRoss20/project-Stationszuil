from tkinter import *
import psycopg2
import random
import json
import requests
import time

"""
In deze module word met behulp van tkinter een stationscherm gemaakt.
Eerst connecten met de database en de laatste 5 berichten in dit bestand krijgen.
Daarna 3 geselecteerde stations kiezen waar de persoon nu is en waar het stationscherm hangt.
Met behulp van API het weer krijgen in het bestand van het gegeven station.
Dan alles met behulp van tkinker in het scherm krijgen.
"""

#Connectie maken met de database
conn = psycopg2.connect(database='DatabaseStationszuil', user='postgres', password='Brett.ross15',
                            host='localhost', port='5432')

con = conn.cursor()

#De gegeven informatie van de database halen en geven. in dit geval de tabel review en de laatste 5 berichten.
con.execute(""" SELECT bericht, naam, station, datumbericht, tijdbericht FROM review
                ORDER BY datumbericht DESC , tijdbericht DESC
                LIMIT 5""")

laatsteberichten = con.fetchall()

print(laatsteberichten)

bericht = random.choice(laatsteberichten)  #Kiest 1 van de 5 berichten uit
print(bericht)


stations = ['Arnhem', 'Utrecht', 'Alkmaar']  #De 3 gekozen stations
randomstation = random.choice(stations)  #Kiest 1 random station uit van de 3 gekozen stations

print(randomstation)

#Functie voor het weer
def weer():
    weer_url = requests.get('https://api.openweathermap.org/data/2.5/weather?q='
                            + randomstation + '&appid=d8b7505e0222715a229b233398f4acfe')  #Website voor het weer
    weer = json.loads(weer_url.content)  #Maakt een json file aan van het weer

    temp = int(weer['main']['temp'] - 273)  #zet de temperatuur om in celsius
    beschrijving = weer['weather'][0]['description']  #Geeft de beschrijving van het weer
    temp_string = str(temp) + str(chr(176))

    weerbericht = []

    weerbericht.append(temp_string)
    weerbericht.append(beschrijving)

    weerbericht = (weerbericht)

    return weerbericht

print(weer())


tijd = time.strftime('%H:%M:%S')  #Noemt de tijd in uur, minuten, seconden
tijdenstation = "Dit is station:"+ " "+ randomstation + "." + " "+ "Tijd: "+ tijd

#Start tkinter op
root = Tk()

root.geometry('800x320')  #Grootte van het scherm
#Laat de tijd en station op het scherm zien
tijdopscherm = Label(root, text=tijdenstation, foreground='blue', relief='groove', font=("Comic Sans", 20))
tijdopscherm.grid(column=0, row=0)
#Laat een tekst zien op het scherm
tekst = Label(root, text='Een bericht van een reiziger op een van onze stations:', relief='groove',
              font=("Comic Sans", 12))
tekst.grid(column=0, row=2)
#Laat het bericht van de reiziger zien
berichtopscherm = Label(root, text=bericht, relief='groove', font=("Comic Sans", 12))
berichtopscherm.grid(column=0, row=3)
#Laat een tekst zien op het scherm
tekst2 = Label(root, text='Dit is het weerbericht:', relief='groove', font=("Comic Sans", 12))
tekst2.grid(column=0, row=4)
#Laat het weerbericht op het scherm zien
weerbericht = Label(root, text=weer(), relief='groove', font=("Comic Sans", 16))
weerbericht.grid(column=0, row=5)
#Laat en tekst zien op het scherm
tekst3 = Label(root, text='Dit station heeft de volgende faciliteiten:', relief='groove', font=("Comic Sans", 12))
tekst3.grid(column=0, row=6)

#Upload een foto naar het scherm
img2 = PhotoImage(file='img_toilet.png')
label = Label(master=root, image=img2)
label.place(x=150, y=200, width=120)
#Upload een foto naar het scherm
img3 = PhotoImage(file='img_ovfiets.png')
label = Label(master=root, image=img3)
label.place(x=300, y=200, width=120)

root.mainloop()

