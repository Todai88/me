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
JSON = False
FILE_OUTPUT = False
OUTPUT_FILE = ""
FILE_INPUT = False
INPUT_FILE = ""
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


def parse():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """

    # Switch through all options
    try:
        global VERBOSE, JSON, FILE_OUTPUT, OUTPUT_FILE, FILE_INPUT


        opts, args = getopt.getopt(sys.argv[1:], "hsv", ["help", "version", "silent", \
                                                        "verbose", "input=", "output=",\
                                                         "json"])

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
            elif opt in ("--output"):
                FILE_OUTPUT = True
                print("ARG: ", arg)
                OUTPUT_FILE = arg
            elif opt in ("--json"):
                JSON = True
            elif opt in ("--input"):
                FILE_INPUT = True
                setInput(arg)
            elif opt in ("--input"):
                print("Printing to: ", arg)
            else:
                assert False, "Unhandled option"
        for arg in args:

            if arg in "get":
                get(''.join(args[1:]))
            elif arg in "ping":
                ping(''.join(args[1:]))
            elif arg in "quote":
                quote()
            elif arg in ("ping-history"):
                history()
            elif arg in ("title"):
                if FILE_INPUT:
                    title(INPUT_FILE)
                else:
                    title(''.join(args[1]))
            elif arg in ("seo"):
                if FILE_INPUT:
                    seo(INPUT_FILE)
                else:
                    seo(''.join(args[1]))
            elif arg in ("image"):
                parseImage(''.join(args[1]))




    except Exception as err:
        print("Error ", err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)
    #print(sys.argv[1])

def setInput(fname):
    """
    Checks if input file exists, if does then reads from it
    """
    #Getting necessary imports
    global INPUT_FILE
    if VERBOSE:
        if os.path.isfile(fname):
            print("File found")
            print("Reading from " + fname)
            INPUT_FILE = fname
        else:
            print("File not found. The quotes are in 'quotes.txt'")
    else:
        if os.path.isfile(fname):
            INPUT_FILE = fname
        else:
            print("File not found.")


def setOutput(output):
    """
    Sets the output target
    """
    #Getting necessary imports

    if VERBOSE:
        if os.path.isfile(OUTPUT_FILE):
            print("File found")
            print("Overwriting file with " + OUTPUT_FILE)
        else:
            print("No file name with filename, creating new")
    with open(OUTPUT_FILE, "w") as f:
        f.write(str(output))

def history():
    """
    prints the ping-history
    """
    #Getting necessary imports
    import sqlite3

    conn = sqlite3.connect("pings.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    for row in cursor:
        print(row)

def quote():
    """
    Gets a quote from the webapi or from a json-file
    """
    #Getting necessary imports
    import requests, json
    from random import randint

    if FILE_INPUT == False:
        URL = "http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php"
        req = requests.get(URL)

        if VERBOSE:
            print("The response code from the server was: ", req.status_code)
            print("\nBelow is the request body: \n\n", req.text)

        quote_obj = req.json()
        print("\nQuote of today is:\n\"{quote}\"\n".format(quote=quote_obj["quote"]))

    else:
        print("READING FROM FILE!")
        with open(INPUT_FILE, "r") as f:
            jobj = json.load(f)
            print("\n********** QUOTE ***************")
            print(jobj['quotes'][randint(0, len(jobj['quotes']))])
            print("********************************")


def ping(URL):
    """
    Pings a client / server and writes to an SQLlite instance
    """
    #Getting necessary imports
    import requests, sqlite3, time

    #Setting up variables
    start = time.time()
    req = requests.head(URL)
    end = time.time()
    db_name = "pings.db"

    #printing result
    if VERBOSE == True:
        print("I'm pinging: ", URL)
        latency = str(round((end - start) * 1000, 2))
        print("Latency: {}ms".format(latency))
    print("Received HTTP response (status code): ", req.status_code)


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
        print("Error ", err)
        print(MSG_USAGE)



def get(URL):
    """
    Gets an entire website and prints to console / file
    """
    #Get necessary imports
    import requests
    from bs4 import BeautifulSoup

    #Setting up variables
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')

    if FILE_OUTPUT:
        soup = BeautifulSoup(req.text, 'html.parser')
        setOutput(soup)
    else:
        print(soup)

def title(URL):
    """
    gets the title of a website / FILE
    """
    #Get necessary imports
    import requests
    from bs4 import BeautifulSoup

    #Setting up variables

    if FILE_INPUT:
        if VERBOSE:
            print("READING FROM FILE!")
        soup = BeautifulSoup(open(URL), "html.parser")
        print(soup.title)
    else:
        req = requests.get(URL)
        soup = BeautifulSoup(req.text, "html.parser")
        print(soup.title)


def seo(URL):
    """
    Analyzes the SEO of a webpage / FILE
    """
    #Get necessary imports
    import requests, json
    from bs4 import BeautifulSoup

    #Getting the soup
    if FILE_INPUT:
        if VERBOSE:
            print("READING FROM FILE!")
        soup = BeautifulSoup(open(URL), "html.parser")

    else:
        req = requests.get(URL)
        soup = BeautifulSoup(req.text, "html.parser")

    #Setting up the variables
    titles = soup.find_all("title")
    h1 = soup.find_all("h1")
    h2 = soup.find_all("h2")
    links = soup.find_all("a")

    #Cleaning up the variables
    titles = [''.join(item.contents).strip() for item in titles]


    if JSON:
        obj = {'Target' : URL, 'Titles(#)' : len(titles), \
                'Titles' : titles, 'H1(#)' : len(h1), 'H2(#)' : len(h2), \
                'Links(#)' : len(links)}
        jdmp = json.dumps(obj)
        jobj = json.loads(jdmp)
        print("\n\n*************JSON******************")
        print("Here is the full object:\n", jobj)
        print("\n\nAnd here is a custom pretty print of it:")
        print("\nTarget    URL \t", jobj['Target'],\
              "\nNo of  titles \t", jobj['Titles(#)'],\
              "\nNo of H1 elem\t", jobj['H1(#)'],\
              "\nNo of H2 elem\t", jobj['H2(#)'],\
              "\nNo of a  elem\t", jobj["Links(#)"])

    else:

        print("\n\nThere were " + str(len(titles)) + " titles, this is the content:")
        print("\n\tString-length in paranthesis!")
        print("**************************************")
        for item in titles:
            print("(" + str(len(item)) + ") \t" + item)

        h1_count = len(h1)
        h2_count = len(h2)
        links_count = len(links)
        print("\n************SEO Content***************")
        print("H1:\t\tH2:\t\tLinks:")
        print(str(h1_count) + "\t\t" + str(h2_count) + "\t\t" + str(links_count))
        print("**************************************")

def parseImage(URL):
    """
    parses the image
    """
    img = getImage(URL)
    img = grayscale(img)
    img_list = parseimg(img)
    print_img(img_list, img.width)

def getImage(URL):
    """
    Gets the image from a user-supplied URL
    """
    from PIL import Image
    import requests
    from io import BytesIO

    response = requests.get(URL)
    img = Image.open(BytesIO(response.content))
    return img

def grayscale(img):
    """
    gray_img:
    Returns a gray-scalled image that can be parsed
    """

    width, height = img.size
    newHeight = int((height * 80) / width)
    newImage = img.resize((80, newHeight))
    newImage = newImage.convert("L")
    return newImage

def parseimg(img):
    """
    Parses the image to a list of ASCII symbols. (I'm using the
                                                  same symbols as the example)
    """
    delims = ['#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
    img_list = []
    allPixels = list(img.getdata())

    for pixelValue in allPixels: #using Mos's algo
        index = int(pixelValue / 25) # 0 - 10
        img_list.append(delims[index])

    return img_list

def print_img(image, width):
    """
    Prints the ASCII list
    """
    image = ''.join(ch for ch in image)
    for c in range(0, len(image), width):
        print(image[c:c + width])

def main():
    """
    Main function to carry out the work.
    """
    startTime = datetime.now()
    parse()
    timediff = datetime.now()-startTime

    if VERBOSE:
        sys.stderr.write("Script executed in {}.{} seconds\n".format(timediff.seconds, timediff.microseconds))

    sys.exit(EXIT_SUCCESS)



if __name__ == "__main__":
    main()
