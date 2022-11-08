from tkinter import *
import psycopg2
import random
import json
import requests
import time


conn = psycopg2.connect(database='DatabaseStationszuil', user='postgres', password='Brett.ross15',
                            host='localhost', port='5432')

con = conn.cursor()

con.execute(""" SELECT bericht, naam, station, datumbericht, tijdbericht FROM review
                ORDER BY datumbericht DESC , tijdbericht DESC
                LIMIT 5""")

laatsteberichten = con.fetchall()

print(laatsteberichten)

bericht = random.choice(laatsteberichten)
print(bericht)


stations = ['Arnhem', 'Utrecht', 'Alkmaar']
randomstation = random.choice(stations)

print(randomstation)


def weer():
    weer_url = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + randomstation + '&appid=d8b7505e0222715a229b233398f4acfe')
    weer = json.loads(weer_url.content)

    temp = int(weer['main']['temp'] - 273)
    beschrijving = weer['weather'][0]['description']
    temp_string = str(temp) + str(chr(176))

    weerbericht = []

    weerbericht.append(temp_string)
    weerbericht.append(beschrijving)

    weerbericht = (weerbericht)

    return weerbericht

print(weer())


tijd = time.strftime('%H:%M:%S')
tijdenstation = "Dit is station:"+ " "+ randomstation + "." + " "+ "Tijd: "+ tijd


root = Tk()

root.geometry('1092x620')

tijdopscherm = Label(root, text=tijdenstation, foreground='blue', relief='groove', font=("Comic Sans", 20))
tijdopscherm.grid(column=0, row=0)

tekst = Label(root, text='Een bericht van een reiziger op een van onze stations:', relief='groove', font=("Comic Sans", 12))
tekst.grid(column=0, row=2)

berichtopscherm = Label(root, text=bericht, relief='groove', font=("Comic Sans", 12))
berichtopscherm.grid(column=0, row=3)

tekst2 = Label(root, text='Dit is het weerbericht:', relief='groove', font=("Comic Sans", 12))
tekst2.grid(column=0, row=4)

weerbericht = Label(root, text=weer(), relief='groove', font=("Comic Sans", 16))
weerbericht.grid(column=0, row=5)

img2 = PhotoImage(file='img_toilet.png')
label = Label(master=root, image=img2)
label.place(x=970, y=0, width=120)

img3 = PhotoImage(file='img_ovfiets.png')
label = Label(master=root, image=img3)
label.place(x=850, y=0, width=120)

root.mainloop()

