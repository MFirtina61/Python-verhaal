from secrets import choice
import time

antwoord_A = ["A", "a"]
antwoord_B = ["B", "b"]
antwoord_C = ["C", "c"]
antwoord_D = ["D", "d"]



    # O T rex ei rennen
def optie_rennen():
    print("Je rent zo snel mogelijk, alleen de T rex had je in de gaten")
    time.sleep(2)
    print("Wil opnieuw?")
    x = input ()
    if x == "ja":
        vraag1()
    else:
        quit()

    # O onderzoeken opgegeten
def optie_verderonderzoeken():
    print("Je bent tijdens het onderzoeken opgegeten")
    time.sleep(2)
    print("Wil opnieuw?")
    x = input ()
    if x == "ja":
        vraag1()
    else:
        quit()

    
    # O terug naar huis met de ei
def optie_huis():
    print("Je loopt voorzichtig weer terug naar de heuvel en je ziet de deur")
    time.sleep(2)
    print("Je gaat naar binnen met de ei, iedereen stont op je te wachten jullie vieren met ze allen een feestje")
    time.sleep(2)
    print("Gefeliciteerd je hebt de missie gehaald!!!")


   # O wachten
def optie_wacht():
    ei = 0
    print("Je bent aan het wachten en je ziet de perfecte moment!")
    time.sleep
    ei += 1
    print("Je hebt" + str(ei) + "ei")
    time.sleep(2)
    print("Je rent zo snel mogelijk en je neemt de ei mee!!! ")
    print(ei = 1)
    time.sleep(2)
    print("""Wat ga je doen?
    A. Verder onderzoeken 
    B. Naar huis """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_verderonderzoeken()

    elif antwoord in antwoord_B:
        optie_huis()



# O andere kant op
def optie_andererichting():
    print("Je loopt de andere kant op na een tijdje hoor je iets bewegen in de bosjes")
    time.sleep(2)
    print("Je kijkt door de bosjes en je ziet de T rex met de ei ")
    time.sleep(2)
    print("""Wat ga je doen?
    A. Ren naar de ei 
    B. Wacht """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_rennen()

    elif antwoord in antwoord_B:
        optie_wacht()

# O weg rennen
def optie_wegrennen():
    print("Je rent zo snel mogelijk weg en dat maakt veel geluid")
    time.sleep(2)
    print("dus de dino rent achter je aan maar de dino is veel sneller")
    time.sleep(2)
    print("Wil opnieuw?")
    x = input ()
    if x == "ja":
        vraag1()
    else:
        quit()


def optie_veranderd():
    print("Hij neemt je mij naar een grot hij begint je te opvoeden als een dino")
    time.sleep(2)
    print("2 jaar later, Je bent veranderd naar een dino")
    quit()

# O liggen
def optie_liggen():
    print("Je licht achter een grote steen ")
    time.sleep(2)
    print("Maar de dino haad je al gezien hij neemt je mee hij heeft je helemaal vast in zijn handen")
    time.sleep(2)
    print("""Wat ga je doen?
    A. Niks 
    B. Proberen te onsnappen """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_veranderd()

    elif antwoord in antwoord_B:
        optie_veranderd()

# O richting dino
def optie_dinorichting():
    print("Je loopt richting de dino")
    time.sleep(2)
    print("en de dino loopt richting jou!")
    time.sleep(2)
    print("""Wat ga je doen?
    A. Ga liggen
    B. Ren weg """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_liggen()

    elif antwoord in antwoord_B:
        optie_wegrennen()


# O onderzoeken 1
def optie_onderzoeken():
    print("Je bent aan het rond lopen in het bos")
    time.sleep(2)
    print("Je ziet in het verte een dino!")
    time.sleep(2)
    print("""Wat ga je doen?
    A. Richting de dino
    B. andere kant op """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_dinorichting()

    elif antwoord in antwoord_B:
        optie_andererichting()


   # S je geeft op
def optie_vast():
    print("Je bent al een tijdje aan het lopen maar je bent zo moe")
    time.sleep(2)
    print("Je bent flauwgevallen, je zit vast in deze wereld")
    quit()


   # S je geeft op
def optie_geefop():
    print("Je zit vast in deze wereld")
    quit()

    # S gedronken
def optie_gedronken():
    print("Je hebt water gedronken je voelt je al veel beter")
    time.sleep(2)
    print("Je moet nog de ei zoeken, alleen je bent echt moe")
    time.sleep(2)
    print("""Wat ga je doen?
    A. Geef op
    B. Verder zoeken """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_geefop()

    elif antwoord in antwoord_B:
        optie_vast()

    # S verder lopen zonder
def optie_geenwater():
    print("Die wormen waren giftig je moest water drinken")
    time.sleep(2)
    print("Wil opnieuw?")
    x = input ()
    if x == "ja":
        vraag1()
    else:
        quit()

    # S verder rennen
def optie_verder():
    print("Je renst zo snel mogelijk alleen de moeder Raptor is veel sneller")
    time.sleep(2)
    print("Je bent opgegeten!")
    time.sleep(2)
    print("Wil opnieuw?")
    x = input ()
    if x == "ja":
        vraag1()
    else:
        quit()


    # S steen gooien
def optie_steen():
    print("Je hebt de steen gemist")
    time.sleep(2)
    print("Wil opnieuw?")
    x = input ()
    if x == "ja":
        vraag1()
    else:
        quit()


    # S weg rennen
def optie_rennen():
    print("Je rent zo snel mogelijk we en de moeder Raptor rent achter je aan")
    time.sleep(2)
    print("Je hebt toevalig een steen in je zak")
    time.sleep(2)
    print("""Wat ga je doen?
    A. Gooi steen
    B. Ren verder """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_steen()

    elif antwoord in antwoord_B:
        optie_verder()

    # S stil staan
def optie_stilstaan():
    print("De moeder Raptor heeft je opgegeten")
    time.sleep(2)
    print("Wil opnieuw?")
    x = input ()
    if x == "ja":
        vraag1()
    else:
        quit()

    # S worm eten
def optie_gegeten():
    print("Ogh je hebt die wormen gegeten en je voelt iets raars")
    time.sleep(2)
    print("Je hebt nu water nodig je ziet een rivier verder op")
    time.sleep(2)
    print("""Wat ga je doen?
    A. Naar de rivier en water drinken
    B. verder gaan lopen """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_gedronken()

    elif antwoord in antwoord_B:
        optie_geenwater()

    # S eiren gegeten
def optie_opzoek():
    print("Tijdens het lopen heb je eiren gevonden je hebt het gelijk opgegten")
    time.sleep(2)
    print("Je hebt de eiren van een Raptor gegeten de Raptor moeder ent achte je aan!")
    time.sleep(2)
    print("""Wat ga je doen!
    A. Stil staan
    B. Weg rennen """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_stilstaan()

    elif antwoord in antwoord_B:
        optie_rennen()

# S opzoek naar eten
def optie_wormen():
    print("Je bent rustig in het bos aan het lopen")
    time.sleep(2)
    print("je ziet wormen op de grond")
    time.sleep(2)
    print("""Ga je ze op eten?
    A. Ja
    B. Nee zoek verder """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_gegeten()

    elif antwoord in antwoord_B:
        optie_opzoek()


# S Blijf
def optie_blijf():
    print("Je bent uitverhongert!")
    time.sleep(2)
    print("Wil opnieuw?")
    x = input ()
    if x == "ja":
        vraag1()
    else:
        quit()

# S schuilen 1
def optie_schuilen():
    print("Je zit al een tijdje onder een boom")
    time.sleep(2)
    print("maar je begint echt veel honger te krijgen")
    time.sleep(2)
    print("""Wat ga je doen?
    A. blijf zitten
    B. ga opzoek naar eten """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_blijf()

    elif antwoord in antwoord_B:
        optie_wormen()

#vraag
def vraag1():
    print (""" Wat  ga je doen?
    A. Wereld onderzoeken
    B. Schuilen van de dinio's """)

    antwoord = input(">>> ")
    if antwoord in antwoord_A:
        optie_onderzoeken()

    elif antwoord in antwoord_B:
        optie_schuilen()

#intro
print("Je zit in een labratorium, ze zijn van plan om een heel groot project uit te voeren")
time.sleep(2)
print("Alleen ze hebben een T Rex ei nodig en jij gaat opzoek naar die ei")
time.sleep(2)
print("Je bent getelporteerd naar de jaar -50000 en je komt der alleen uit met de ei")
time.sleep(2)
print("Je bent op een heuvel en je kijkt om je heen en je ziet allemaal dino's")
vraag1()












