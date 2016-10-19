#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Global variables
import os, sys
from start import init_game
from game import prepare_loop

PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Joakim Bajoul Kakaei"
EMAIL = "joakim@kimput.com"
WEBSITE = "http://portfolio.kimput.com"
VERSION = "1.0.0"
HELP = """
#############
##
##  Usage:
##      {program} [options] name
##
#############
##
##  Options:
##      -h, --help     |#|      Display this help message.
##      -i, --info     |#|      Displays the game idea and a description
##                                  of the game.
##      -v, --version  |#|      Print version and exit.
##      -a, --about    |#|      Prints a short introduction about me.
##      -c, --cheat    |#|      Shows you the way and displays
##                                  the answers to the puzzles.
#############
""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

ABOUT = """

Hi,

My name is Joakim Bajoul Kakaei.
I'm a Software Engineer, born in Sweden, working in the UK.

As an emerging developer and owner of Kimput.com,
I hope to bring a new way of
bridging the gap between a simple,
intuitive user experience and flexible design.

For further information you can contact me at {email}
or check out my portfolio website {website}.

I'd be happy to answer any questions!
""".format(email=EMAIL, website=WEBSITE)

INFO = """
Ragnar's great revenge.

Since having been captured, compiled and executed
countless times Ragnar - the main antagonist in this
course has now decided to unleash his fury at You!

You will have to solve his puzzles to escape from
his dungeon of DOOOOOOOM! :p

*Actually it is quite simple stuff*
"""

CHEATS = """
You sure you want to cheat? I'll add the cheats later
(shortest route, puzzle answers)
"""


#Player global variables
PLAYER = {}
ROOM = {}
def parseOpts():
    #Get imports
    import getopt

    #Loop throug the options, if any.
    try:

        opts, args = getopt.getopt(sys.argv[1:], "hivac", ["help", "info", "version",\
                                                     "about", "cheat"])
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(HELP)
            elif opt in ("-a", "--about"):
                print(ABOUT)
            elif opt in ("-v", "--version"):
                print("The version of the game is: ", VERSION)
            elif opt in ("-i", "--info"):
                print(INFO)
            elif opt in ("-c", "--cheat"):
                print(CHEATS)
    except Exception as err:
        print("Error ", err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)

def main():
    """
    Main function to carry out the work.
    """
    parseOpts()
    game_obj = init_game()
    print(game_obj)
    prepare_loop(game_obj)

if __name__ == "__main__":
    main()
