"""
main game module
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tictoe import init_tic
from crypto import init_crypto

#initiating the globals
DIRECTIONS = ["n", "norr", "v", "väst", "s", "syd", "ö", "öst"]
PLAYER = {}
ROOM = {}
FINISHED = False
HELP = """
~~~~~~~~~~~~~~ INSTRUKTIONER ~~~~~~~~~~~~

##  Du kan interagera med alla objekt i stora BOKSTÄVER
##           exempel: GRYTA ('ta gryta'), ÖST (gå ÖST) osv.
##
##   KOMMANDO:              GÖR:
##   i, info            Skriver ut rumsbeskrivningen.
##   gå (riktning)      Går i den riktningen (ex: 'N' eller 'norr')
##   h, hjälp           Skriver ut denna hjälp-sträng.
##   se                 Berättar vad du kan interagera med.
##   l, ledtråd         Ger dig en ledtråd om rummet.
##   spara, save        Sparar ditt spel
##   ta <objekt>        Tar objektet, om det är tillgängligt.
##   sl, släpp <objekt> Släpper objektet om det är använt.
##   inv, inventarier   Präntar ut ditt inventarier
##   o, objekt          Skriver ut de objekten som finns rummet.
##   t, titta <objekt>  Skriver ut beskrivningen av ett objekt
##   ö, öppna <objekt>  Öppnar ett objekt, om möjligt.
##   s, sparka <objekt> Sparka ett objekt, om möjligt.
##   f, flytta <objekt> Flyttar på ett objekt, om möjligt.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


FINISH = """
#################################

DU KLARADE SPELET! RAGNAR ÄR BESEGRAD OCH DU KOMMER TILLBAKA TILL DITT VANLIGA LIV.

###############################"""

HINTS = {1 : {"used" : False, "advice" : "Du kan inte slänga föremål utan att ha använt dem."},
         2:  {"used" : False, "advice" : "Försök inte att förstöra mitt spel! :("},
         3:  {"used" : False, "advice" : "Använd dig utav 'god' kommandot för"\
                                        "att få tillgång till alla rum"},
         4: {"used" : False, "advice"   : "Glöm inte bort att du kan använda "\
                                        "dig av getopt vid start."},
         5: {"used" : False, "advice"   : "Tack för en grym kurs!"}}

def prepare_loop(game_obj):
    """
    startar spel-loopen.
    """

    cls()
    setup(game_obj)
    printInstruction()

    while(FINISHED == False):
        getAction()

    win()

def win():
    """
    präntar win-strängen
    """

    print(FINISH)

def cls():
    """
    Rensar upp skärmen för att göra det lite mer cleant
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def setup(obj):
    """
    Sätter upp spelaren
    """
    global PLAYER, ROOM
    PLAYER = obj[0]
    ROOM = obj[1]

##
## Generella print-funktioner.
##

def printDesc():
    """
    präntar information om rummet
    """

    print("\n############## BESKRIVNING ##############\n")
    print(ROOM["description"])
    print("\n#########################################")

def printInstruction():
    """
    präntar hjälp INSTRUKTIONER
    """
    print(HELP)

def printQuestion():
    """
    präntar frågor
    """
    print(ROOM["question"])

def check_access(room_id):
    """
    Denna funktion 'peekar' till rummet som man ska till
    för att se utifall man har tillgång till det rummet.
    Detta genom att se utifall ID:t på rummet finns i spelarens
    access
    """
    global FINISHED

    trying = True
    # Se efter om det är en specifik fråga - ett spel.
    if room_id not in PLAYER["access"]:
        if ROOM["puzzle"] == "tic".upper():
            condition = init_tic()
            if (condition):
                PLAYER["access"].insert(len(PLAYER["access"]), room_id)
                trying = False
                return True
            else:
                trying = False
                return False
        elif ROOM["puzzle"] == "crypto".upper():

            init_crypto()
            PLAYER["access"].insert(len(PLAYER["access"]), room_id)
            trying = False
            return True
        #om inte (som i rum 1). Så visas en snabb sträng (fråga)
        #och spelaren måste svara på den.
        else:
            while trying:
                print(ROOM["puzzle"])
                svar = input("Vad gör du?\n")
                if svar.upper() == ROOM["answer"]:
                    PLAYER["access"].insert(len(PLAYER["access"]), room_id)
                    PLAYER["solved"].insert(len(PLAYER["solved"]), ROOM["id"])
                    trying = False
                    return True
                elif svar.upper() == "EXIT":
                    trying = False
                    return False
                else:
                    cls()
                    print("Fel handling! Pröva igen...")
    else:
        if room_id == 10:
            cls()
            print(FINISH)
            FINISHED = True

        return True

def valid_move(action):
    """
    Först ser funktionen efter utifall det är en korrent sträng
    (om riktningen är korrekt formatterad).
    Ser efter om riktningen finns i rummet spelaren befinner sig i.
    Om det finns, så skickas datan vidare till ovan funktion.
    """
    if action in ("n", "norr"):
        if ("north" in ROOM):
            if check_access(ROOM["north"]):
                changeRoom(ROOM["north"])
                return True
            else:
                cls()
                printError("Du får inte tillgång till rummet. Nedan har du" + \
                            " rumsbeskrivningen.")
                printDesc()
        else:
            cls()
            printError("Det finns inget rum i den riktningen!")
            printDesc()
    elif action in ("ö", "öst"):
        if ("east" in ROOM):
            if check_access(ROOM["east"]):
                changeRoom(ROOM["east"])
                return True
            else:
                cls()
                printError("Du får inte tillgång till rummet. Nedan har du"+\
                            " rumsbeskrivningen.")
                printDesc()
        else:
            cls()
            printError("Det finns inget rum i den riktningen!")
            printDesc()
    elif action in ("s", "syd"):
        print(PLAYER["access"])
        if ("south" in ROOM):
            if check_access(ROOM["south"]):
                changeRoom(ROOM["south"])
                return True
            else:
                cls()
                printError("Du får inte tillgång till rummet. Nedan har du" +\
                            " rumsbeskrivningen.")
                printDesc()
        else:
            cls()
            printError("Det finns inget rum i den riktningen!")
            printDesc()
    elif action in ("v", "väst"):
        if ("west" in ROOM):
            if check_access(ROOM["west"]):
                changeRoom(ROOM["west"])
                return True
            else:
                cls()
                printError("Du får inte tillgång till rummet. Nedan har du"+\
                            " rumsbeskrivningen.")
                printDesc()
        else:
            cls()
            printError("Det finns inget rum i den riktningen!")
            printDesc()
    else:
        cls()
        printError("Ogiltig riktning. NORR, ÖST, SYD, VÄST samt N,Ö,S,V är OK.")
        return False
    return False

def changeRoom(new_room):
    """
    byter rum, utifall användaren har tillgång till rummet.
    Denna funktion sköter också victory-condition.
    Om rummet spelaren ska till är 10, så stoppar den loopen.
    """
    import json
    global ROOM, FINISHED

    if new_room == 10:
        FINISHED = True

    with open('rooms.json') as room_data:
        obj = json.load(room_data)

    room_obj = [item for item in obj["rooms"] if \
                  item["id"] == new_room]

    ROOM = room_obj[0]
    PLAYER["room"] = new_room
    changeDescription()

def printError(error_string):
    """
    Präntar en välformatterad error-sträng
    """
    print("################ ERROR ####################\n")
    print(error_string)
    print("\n##########################################\n")

def print_inv():
    """
    skriver ut inventory
    """
    inv = ', '.join(PLAYER["inventory"])
    print("I din ryggsäck ligger det:", inv)

def save_player():
    """
    Sparar spelaren i players.json med hjälp av en json-dump.
    """

    import json

    with open('player.json', 'r+') as f:
        obj = json.load(f)
        #setting up new player
        #appending to already existing json
        obj["players"][PLAYER["id"] - 1] = PLAYER
        print(obj)
        #clearing previous json
        f.seek(0)
        f.truncate()
        #writing to json
        json.dump(obj, f, indent=2)
    print("Sparat spelet!")

def item_exists(item_name):
    """
    Ser efter utifall föremålet finns i rummet.
    Om det finns, så interagerar spelaren med det.
    """
    print(item_name)
    flag = [item_name in item["item"] for item in ROOM["objects"]\
                    if item_name in item["item"]]
    if flag != []:
        if item_name not in PLAYER["inventory"]:
            ROOM["description"] = ROOM["alt_description"]
            PLAYER["interacted"].insert(len(PLAYER["interacted"]), ROOM["id"])
            return True
        else:
            printError("Du har redan en / ett " + item_name + " i din ryggsäck.")
            return False
    else:
        cls()
        printError("Det finns inget föremål med det namnet i det här rummet.")
        return False

def changeDescription():
    """
    Ändrar det rummet som är in-memory's beskrivning
    beroende på utifall användaren
    a.) har löst rummet (om ragnar varit där).
    b.) om spelaren har interagerat med något.
    """

    if "solved_ragnar" in ROOM:
        if ROOM["id"] in PLAYER["solved"]:
            ROOM["description"] = ROOM["solved_ragnar"]
    elif "alt_description" in ROOM:
        if ROOM["id"] in PLAYER["interacted"]:
            ROOM["description"] = ROOM["alt_description"]

def drop_item(item_name):
    """
    släpper ett objekt av spelarens val.
    Kan bara genomföras utifall användaren har använt föremålet.
    """

    item_name = item_name.strip()
    if item_name in PLAYER["inventory"]:
        if item_name in PLAYER["used"]:
            index = PLAYER["inventory"].index(item_name)
            PLAYER["inventory"].pop(index)
            print("Du har släppt grytan.")
        else:
            print("Du måste ha använt ditt föremål innan du kan slänga det!")
    else:
        print("Föremålet finns inte i din ryggsäck. Du kanske stavade fel?")

def use_item(item):
    """
    Använder föremålet.
    """
    if item in PLAYER["inventory"]:
        temp = item.upper()
        print("Item exists in inventory")

        if ROOM["id"] == 2 and temp == "GRYTA":
            cls()
            print("Du gav grytan till Ragnar som glupskt äter upp den och går söderut.")
            PLAYER["access"].insert(len(PLAYER["access"]), 3)
            PLAYER["solved"].insert(len(PLAYER["solved"]), ROOM["id"])
            PLAYER["used"].insert(len(PLAYER["used"]), item)
            changeDescription()
        elif ROOM["id"] == 8 and temp == "NYCKEL":
            cls()
            print("Du sätter nyckeln i låset och hör hur mekanismen klickar till. " + \
                  "Dörren är upplåst.")
            PLAYER["access"].insert(len(PLAYER["access"]), 9)
            PLAYER["solved"].insert(len(PLAYER["solved"]), ROOM["id"])
            PLAYER["used"].insert(len(PLAYER["used"]), item)
            changeDescription()
        elif ROOM["id"] == 9 and temp == "SVÄRD":
            cls()
            print("Du ger svärdet till draken och han tackar så gott. Här är vi alla vänner!"\
                  "Förutom Ragnar, som draken äter upp.")
            PLAYER["access"].insert(len(PLAYER["access"]), 10)
            PLAYER["solved"].insert(len(PLAYER["solved"]), ROOM["id"])
            PLAYER["used"].insert(len(PLAYER["used"]), item)
            changeDescription()
        else:
            print("Det finns inget att använda " + item + " på i detta rummet...")

def print_obj():
    """
    Skriver ut alla föremål som användaren kan interagera med i rummet.
    """
    for item in ROOM["objects"]:
        print("Namn: " + item["item"] + "\n")


def print_obj_details(item_name):
    """
    Skriver ut ett föremåls detaljer.
    """
    print(item_name)
    item = [items for items in ROOM["objects"]\
                if item_name in items["item"]]
    print("############ DETALJER #############\n")
    print("Objekt:\t\t" + item[0]["item"])
    print("Detaljer:\t"+ item[0]["description"])
    print("\n############ DETALJER #############")
        #flag = [item_name in item["item"] for item in ROOM["objects"]\
        #                if item_name in item["item"]]

def open_object(item_name):
    """
    Öppnar ett objekt, om möjligt.
    """
    item = [items for items in ROOM["objects"]\
                if item_name in items["item"]]
    if len(item) != 0:
        item = item[0]
        if item["openable"] == True:
            cls()
            print(item["open"])
            ROOM["description"] += "\nDörren / dörrarna står öppna."
        else:
            print("Du kan inte öppna " + item_name)
    else:
        print(item_name + " finns inte i rummet ")
        print_obj()

def kick_object(item_name):
    """
    Sparkar / tar sönder ett föremål, om möjligt.
    """
    item = [items for items in ROOM["objects"]\
                if item_name in items["item"]]
    if len(item) != 0:
        item = item[0]
        if item["kickable"] == True:
            cls()
            print(item["destroyed"])
            PLAYER["interacted"].insert(len(PLAYER["interacted"]), ROOM["id"])
            changeDescription()
        else:
            if len(item["destroyed"]) != 0:
                print(item["destroyed"])
            else:
                printError("Du kan inte ta sönder " + item_name)


    else:
        print(item_name + " finns inte i rummet ")
        print_obj()

def print_see():
    """
    Präntar ut alla objekt som kan vara relevanta.
    """
    for item in ROOM["objects"]:
        print("#####\nFöremål:\t" + item["item"] +"\nInteraktion:\t"\
                +item["interact"] + "\n#####\n")

def move_object(item_name):
    """
    Flyttar på ett objekt, om det kan flyttas på.
    """
    item = [items for items in ROOM["objects"]\
                if item_name in items["item"]]

    if len(item) != 0:
        item = item[0]
        if item["moveable"] == True:
            cls()
            print(item["move"])
            PLAYER["interacted"].insert(len(PLAYER["interacted"]), ROOM["id"])
            changeDescription()
        else:
            cls()
            if len(item["move"]) != 0:
                printError(item["move"])
            else:
                printError("Du kan inte flytta på " + item_name)

    else:
        print(item_name + " finns inte i rummet ")
        print_obj()

def EGM():
    """
    Ger spelaren God-mode.
    """
    print("You enter GOD MODE!!!!")
    PLAYER["access"] = [1, 2, 3, 4, 5, 6, 7, 8]
    PLAYER["solved"] = [1, 2, 3, 4, 5, 6, 7, 8]
    PLAYER["interacted"] = [1, 2, 3, 4, 5, 6, 7, 8]

def print_hint():
    """
    Skriver ut en hint.
    Om alla hintar har skrivts ut, så resettas
    dictionary:n så att de kan skrivas ut igen.
    """

    p_hint = ""
    for item in HINTS.items():
        if item[1]["used"] == False:
            p_hint = item

    #p_hint = [item in item for item in HINTS\
    #            if HINTS[item]["used"] == False]

    if p_hint == "":
        for item in HINTS.items():
            item[1]["used"] = False
        print_hint()

    else:
        print("### LEDTRÅD: " + p_hint[1]["advice"])
        p_hint[1]["used"] = True


def getAction():
    """
    Huvudsaklig loop.
    Denna loop körs tills dess att spelaren antingen gett upp eller vunnit.
    Den parsar spelarens val mycket likt hur marvin-labbarna sköts tidigare.
    Med skillnad att det finns en klar prioritering (de längsta meningarna
    har högst prio för att säkerställa att inte felaktig handling genomförs).
    """

    valid = False
    printDesc()
    while (valid == False): #Anledningen till att jag kör på descending
                            # choice är för att skapa en slags prioritet
        choice = input("Vad vill du göra?\n")

        if choice.upper() in ("H", "HJÄLP"):
            cls()
            printInstruction()
            valid = True

        elif choice.upper() in ("SAVE", "SPARA"):
            save_player()

        elif choice[:11].upper() == ("INVENTARIER"):
            print_inv()

        elif choice[:6].upper() == "LEDTRÅD":
            print_hint()
            valid = True

        elif choice[:6].upper() == ("FLYTTA"):
            move_object(choice[6:].strip())
            valid = True

        elif choice[:6].upper() == ("SPARKA"):
            print(choice[6:].strip())
            kick_object(choice[6:].strip())
            valid = True

        elif choice[:6].upper() == ("ANVÄND"):
            use_item(choice[6:].strip())
            valid = True

        elif choice[:6].upper() == ("OBJEKT"):
            print_obj()

        elif choice[:5].upper() == ("TITTA"):
            print_obj_details(choice[6:].strip())

        elif choice [:5].upper() == ("SLÄPP"):
            drop_item(choice[5:])

        elif choice[:5].upper() == "ÖPPNA":
            open_object(choice[6:].strip())
            valid = True

        elif choice[:3].upper() == ("INV"):
            print_inv()

        elif choice [:3].upper() == ("GOD"):
            EGM()
            valid = True


        elif choice[:4].upper() == ("INFO"):
            cls()
            valid = True

        elif choice[:2].upper() == ("SL"):
            drop_item(choice[2:])

        elif choice[:2].upper() == ("SE"):
            print_see()

        elif choice [:2].upper() == ("TA"): #tvungen att köra == då det kan finnas fall
            if item_exists(choice[3:]): #då 't' ger 'ta'
                PLAYER["inventory"].insert(len(PLAYER["inventory"]), choice[3:].strip())
                valid = True
                cls()
                print("Du tog upp ", choice[3:])

        elif choice[:2].upper() == ("GÅ"):
            if valid_move(choice[3:]):
                valid = True
                cls()

        elif choice[:1].upper() == 'Ö':
            open_object(choice[1:].strip())
            valid = True

        elif choice[:1].upper() == ("A"):
            print(choice[2:])
            use_item(choice[2:].strip())
            valid = True

        elif choice[:1].upper() == ("L"):
            print_hint()
            valid = True

        elif choice[:1].upper() == ("T"):
            print_obj_details(choice[2:].strip())

        elif choice[:1].upper() == ("F"):
            move_object(choice[2:].strip())
            valid = True

        elif choice[:1].upper() == ("S"):
            kick_object(choice[2:].strip())
            valid = True

        elif choice[:1].upper() == ("O"):
            print_obj()

        elif choice[:1].upper() == ("I"):
            cls()
            valid = True


        else:
            cls()
            printError("Ogiltigt val. Nedan ser du hjälp-strängen.")
            printInstruction()
