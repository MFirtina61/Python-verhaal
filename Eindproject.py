from secrets import choice
import time
from turtle import begin_fill 

antwoord_A = ["A", "a"]
antwoord_B = ["B", "b"]
antwoord_C = ["C", "c"]
antwoord_D = ["D", "d"]


#onderzoeken 1
def optie_onderzoeken():
    print("Je bent aan het rond lopen in het bos")
    time.sleep(2)
    print("Je ziet in het verte een dino!")
    time.sleep(2)
    print("""Wat ga je doen?
    A. Richting de dino
    B. andere kant op """)


# S Blijf
def optie_geenwater():
    print("Die wormen waren giftig je moest water drinken")
    time.sleep(2)
    print("Wil opnieuw?")
    x = input ()
    if x == "ja":
        Begin()
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
        optie_gegeten()

    elif antwoord in antwoord_B:
        optie_geenwater()

    # S zoek verder
def optie_opzoek():
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

# S opzoek naar eten
def optie_opzoek():
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
        Begin()
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
        optie_opzoek()

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












