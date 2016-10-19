#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def init_game():
    try:
        player = get_player()
        room = get_room()
        return [player, room]
    except Exception as err:
        print("Error ", err)

def get_room():
    #imports
    import json
    desc = ""
    global ROOM

    with open('rooms.json') as room_data:
        obj = json.load(room_data)
        room_obj = [item for item in obj["rooms"] if \
                      item["id"] == LOC]
        #setting up the room
    return room_obj[0]

def get_player():

    obj = ""
    start_opt = input("Vill du ladda ett spel (Y/N)?\n")
    if start_opt.lower() == "n" or start_opt.lower() == "no":
        player_name = input("Vad är ditt namn?\n")
        player_obj = new_game(player_name)
    elif start_opt.lower() == "y" or start_opt.lower() == "yes":
        player_name = input("Vad var ditt namn?\n")
        player_obj = load_game(player_name)

        if player_obj == []:
            print("\nOBS!! Ingen spelare med det namnet. Startar nytt spel. OBS!!\n")
            player_obj = new_game(player_name)
    else:
        print("Inget korrekt alternativ. Startar nytt spel.")
        player_obj = new_game(input("Vad är ditt namn?\n"))

    return player_obj
def new_game(player_name):
    #imports
    import json, os
    #setting up global
    global NAME, LOC, ID, INVENTORY, ACCESS
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("Välkommen, ", player_name)
    print("\nNu ska vi bara skapa en ny sparfil åt dig!",\
          "\nDu loggar in med ditt namn vid senare tillfällen!")
    print("~~~~~~~~~~~~~~~~~~~~~")
    with open('player.json', 'r+') as f:
        obj = json.load(f)
        amt = [item for item in obj["players"]]
        #setting up new player
        p_obj =  {"id" : len(amt) + 1, "name" : player_name, "room" : 1,\
                 "inventory" : [],\
                 "access" :  []\
                }

        #appending to already existing json
        obj["players"].append(p_obj)
        #clearing previous json
        f.seek(0)
        f.truncate()
        #writing to json
        json.dump(obj, f, indent=2)
    return p_obj
def load_game(player_name):
    #Necessary imports
    import json
    #setting up globals
    global NAME, LOC, ID, INVENTORY, ACCESS

    with open('player.json') as player_data:
        obj = json.load(player_data)

    player_obj = [item for item in obj["players"] if \
                  item["name"] == player_name]
    if player_obj != []:
        NAME = player_obj[0]["name"]
        LOC = player_obj[0]["room"]
        ID = player_obj[0]["id"]
        INVENTORY = player_obj[0]["inventory"]
        ACCESS = player_obj[0]["access"]
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("Välkommen tillbaka, ", player_name) 
    print("~~~~~~~~~~~~~~~~~~~~~")
    return player_obj[0] if player_obj != [] else []
