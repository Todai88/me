#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
##   KOMMANDO:          GÖR:
##   i, info         Skriver ut rumsbeskrivningen.
##   gå (riktning)   Går i den riktningen (ex: 'N' eller 'norr')
##   h, hjälp        Skriver ut denna hjälp-sträng.
##   se              Berättar vad du kan interagera med.
##   l, ledtråd      Ger dig en ledtråd om rummet.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
def prepare_loop(game_obj):
    global FINISHED
    setup(game_obj)
    printInstruction()
    printDesc()
    while(FINISHED == False):
        getAction()

def cls():
    import os
    os.system('cls' if os.name=='nt' else 'clear')

def setup(obj):
    global PLAYER, ROOM
    PLAYER = obj[0]
    ROOM = obj[1]

def printDesc():
    print("\n############## BESKRIVNING ##############\n")
    print(ROOM["description"])
    print("\n#########################################")

def printInstruction():
    print(HELP)
def printQuestion():
    print(ROOM["question"])

def check_access(room_id):
    trying = True
    if room_id not in PLAYER["access"]:
        while trying:
            print(ROOM["puzzle"])
            svar = input("Vad gör du?\n")
            if svar.upper() == ROOM["answer"]:
                PLAYER["access"].insert(len(PLAYER["access"]), room_id)
                trying = False
                return True
            elif svar.upper() == "EXIT":
                trying = False
                return False
            else:
                print("Fel handling! Pröva igen...")

def valid_move(action):
    if action in ("n", "norr"):
        if ("north" in ROOM):
            if check_acces(ROOM["north"]):
                changeRoom(ROOM["north"])
                return True
            else:
                return False
        else:
            return False
    elif action in ("ö", "öst"):
        if ("east" in ROOM):
            if check_access(ROOM["east"]):
                changeRoom(ROOM["east"])
                return True
            else:
                return False
        else:
            return False
    elif action in ("s", "syd"):
        if ("south" in ROOM):
            changeRoom(ROOM["south"])
            return True
        else:
            return False
    elif action in ("v", "väst"):
        if ("west" in ROOM):
            changeRoom(ROOM["west"])
            return True
        else:
            return False
    else:
        return False

def changeRoom(new_room):
    import json
    print("CHAAAANGE ROOM")
    global ROOM
    with open('rooms.json') as room_data:
        obj = json.load(room_data)

    player_obj = [item for item in obj["rooms"] if \
                  item["id"] == new_room]

    ROOM = player_obj[0]
    
def getAction():
    valid = False

    while (valid == False):
        choice = input("Vad vill du göra?\n")

        if choice in ("h", "hjälp"):
            cls()
            printInstruction()
            valid = True
        elif choice in ("i", "info"):
            cls()
            printDesc()
            valid = True
        elif choice[:2] in ("gå"):
            if valid_move(choice[3:]):
                valid = True
                cls()
                printInstruction()
                printDesc()
            else:
                cls()
                print("##########################################\n")
                print("Ogiltigt riktig. Nedan ser du rumsbeskrivningen:")
                print("\n##########################################\n")
                printDesc()
        else:
            cls()
            print("##########################################\n")
            print("Ogiltigt val. Nedan ser du hjälp-strängen:")
            print("\n##########################################\n")
            printInstruction()
