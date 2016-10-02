#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin-cli
"""
import sys
import os
from datetime import datetime
import getopt

#
#
# Setting up global variables
#
#

VERBOSE = False
EXIT_SUCCESS = 0    #Successful exit
EXIT_USAGE = 1      #Unsuccessful due to incorrect args
EXIT_FAILED = 2     #Unsuccessful due to error during execution

#
# Add some stuff about this script (taken from example/cli)
#


PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Joakim Bajoul Kakaei"
EMAIL = "joakim@kimput.com"
VERSION = "1.0.0"
USAGE = """
##  Program {program}.
##  By {author} ({email}),
##  Version {version}.
##
#############
##
##  Usage:
##      {program} [options] name
##
#############
##
##  Options:
##      -h, --help     |#|      Display this help message.
##
##      -s, --silent   |#|      Do not display any details or
##                                    statistics about the execution.
##      -v, --version  |#|      Print version and exit.
##
##      --verbose      |#|      Print additional information
##                                    about the program run-time.
""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)


def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    sys.exit(exitStatus)



def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)


def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """

    # Switch through all options
    try:
        global VERBOSE

        opts, args = getopt.getopt(sys.argv[1:], "hsv", ["help","version","silent", "get=", "ping=", "verbose", "input=", "output=", "json", "quote", "ping-history"])
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                printUsage(EXIT_SUCCESS)

            elif opt in ("-s", "--silent"):
                VERBOSE = False

            elif opt in ("-v", "--version"):
                printVersion()

            elif opt in ("--verbose"):
                print("VERBOSE!!")
                VERBOSE = True
            elif opt in ("--get"):
                get(arg)
            elif opt in ("--ping"):
                ping(arg)
            elif opt in ("--quote"):
                quote()
            elif opt in ("--input"):
                print("Printing to: ", arg)
            elif opt in ("--ping-history"):
                history()
            else:
                assert False, "Unhandled option"


    except Exception as err:
        print("Error " ,err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)
    #print(sys.argv[1])

def history():
    #Getting necessary imports
    import sqlite3

    conn = sqlite3.connect("pings")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    for row in cursor:
        print(row)

def quote():
    #Getting necessary imports
    import requests

    URL = "http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php"
    req = requests.get(URL)

    if VERBOSE:
        print("The response code from the server was: ", req.status_code)
        print("\nBelow is the request body: \n\n", req.text)

    quote = req.json()
    print("\nQuote of today is:\n\"{quote}\"\n".format(quote=quote["quote"]))



def ping(URL):
    #Getting necessary imports
    import requests, sqlite3, time

    #Setting up variables
    start = time.time()
    req = requests.head(URL)
    end = time.time()
    db_name = "pings.db"
    table_name = "history"

    #printing result
    if VERBOSE == False:
        print("I'm pinging: ", URL)
        print("Received HTTP response (status code): ", req.status_code)
    latency = str(round((end - start) * 1000, 2))

    print("Latency: {}ms".format(latency))

    #
    # opening db connection
    #
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        #setting up the create-string
        sql_create = "CREATE TABLE IF NOT EXISTS history (url TEXT, latency TEXT, status INTEGER)"
        #setting up the insert-string
        aTuple = (str(URL), str(latency), str(req.status_code))
        sql_insert = "INSERT INTO history (url, latency, status) VALUES (?, ?, ?)"
        #sending the query
        cursor.execute(sql_create)
        cursor.execute(sql_insert, aTuple)

        if VERBOSE is True:
            select = conn.execute("SELECT url, latency, status FROM history")
            print("IM IN")
            for row in select:
                print(row)
        conn.commit()
        conn.close()
    except Exception as err:
        print("Error " ,err)
        print(MSG_USAGE)



def get(URL):
    #Get necessary imports
    import requests
    from bs4 import BeautifulSoup

    #Setting up variables
    req = requests.get(URL)
    soup = BeautifulSoup(req.text)


    print(soup)

def parseArgs():

    try:
        arg = sys.argv[1]

        if(arg == "get"):
            print(sys.argv)
    except Exception as err:
        print("kalle")
def main():
    """
    Main function to carry out the work.
    """
    startTime = datetime.now()
    parseOptions()
    #parseArgs()
    timediff = datetime.now()-startTime

    if VERBOSE:
        sys.stderr.write("Script executed in {}.{} seconds\n".format(timediff.seconds, timediff.microseconds))

    sys.exit(EXIT_SUCCESS)



if __name__ == "__main__":
    main()
