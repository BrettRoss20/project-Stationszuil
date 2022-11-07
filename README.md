# project-Stationszuil
Module 1: Zuil
Op een zuil op een willekeurig NS-station kunnen reizigers hun bericht van maximaal 140 karakters invoeren. Het bericht moet worden opgeslagen in een tekstbestand met een logische structuur. Sla de onderstaande gegevens op in een gestructureerd tekstbestand:

het bericht;
de datum en tijd van het bericht;
de naam van de reiziger – als de reiziger geen naam invult, gebruik dan als naam ‘anoniem’;
het station – deze locatie van de zuil mag in de module zelf worden vastgelegd op basis van een random choice van drie stations. De computer (jouw python computer programma) kiest dan één station uit deze lijstlijst downloaden  en dat station wordt dan gekoppeld aan het bericht.
Deze module werkt met een Command Line Interface (CLI). Dit mag gewoon gestart worden vanuit PyCharm.

Module 2: Moderatie
Voordat een bericht ook daadwerkelijk op het stationshalscherm wordt gezet, wordt er door een moderator van de NS naar de berichten gekeken. De moderator kan een bericht goed- of afkeuren. Alleen goedgekeurde berichten worden gepubliceerd op het stationshalscherm.

Deze module leest de berichten uit het gestructureerde tekstbestand (zoals beschreven bij module 1) in, beginnend bij het oudste bericht. Na beoordeling door een moderator wordt het hele bericht (inclusief datum, tijd, naam en station) naar een database geschreven. Daarnaast wordt de volgende data toegevoegd:

of het bericht is goedgekeurd of afgekeurd;
de datum en tijd van beoordeling;
de naam van moderator die het bericht heeft beoordeeld;
het email-adres van de moderator.
Deze module werkt met een Command Line Interface (CLI). Dit mag gewoon gestart worden vanuit PyCharm.

Daarnaast moet voor de werking van deze module een database worden gemaakt en gebruikt. Het ontwerp van deze database omvat een conceptueel, een logisch en een fysiek datamodel. De database moet vervolgens worden gerealiseerd in PostgreSQL. De gegevens worden gelezen uit het CSV bestand en aangevuld met de moderatorgegevens en daarna weggeschreven in de database. Het CSV-bestand wordt daarna leeggemaakt.

Module 3: Stationshalscherm
In elke stationshal van Nederland komt een stationshalscherm te hangen. Op dit scherm worden de geplaatste berichten uit heel Nederland getoond:

De berichten worden getoond op chronologische volgorde van invoeren. Alleen de laatste 5 berichten worden getoond.
Ook worden de beschikbare faciliteiten op het station getoond op het scherm. Het gaat hierbij om het station waar het bericht is geschreven. Een station heeft één of meer van de volgende faciliteiten: OV-fietsen, lift, toilet en P+R. De beschikbare faciliteiten staan in deze tabeltabel downloaden, deze moet je toevoegen aan je database. Je kunt eventueel gebruik maken van deze iconeniconen downloaden.
Ten slotte wordt op het stationshalscherm de weersvoorspelling op de locatie van het station getoond. Het gaat hierbij om het station waar het stationshalscherm hangt. Voor het ophalen van de weersvoorspelling maak je gebruik van de OpenWeatherMap API (https://openweathermap.org/Koppelingen naar een externe site.).
Het is belangrijk dat het stationshalscherm er goed uitziet, dus deze module werkt met een Graphical User Interface (GUI), in principe met behulp van Tkinter. Zorg dat je bij het starten van dit stationsscherm kunt kiezen voor één van de stations die jij gekozen hebt in module 1.
