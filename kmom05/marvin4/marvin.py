"""
marvin
"""

#!/usr/bin/env python3
from random import randint
import math


def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
                _______
               _/       \_
              / |       | \
             /  |__   __|  \
            |__/((o| |o))\__|
            |      | |      |
            |\     |_|     /|
            | \           / |
             \| /  ___  \ |/
              \ | / _ \ | /
               \_________/
                _|_____|_
           ____|_________|____
          /                   \
    """


def menu():
    """
    Display the menu with the options that Marvin can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage())
    print("Welcome.\nMy name is Ragnar.\nWhat can I do for you?\n")
    print("Try Ragnar's quote-machine by entering any input that has 'citat' in it!")
    print("1) Present yourself to Ragnar.")
    print("2) Have Ragnar calculate your minimum age (in seconds).")
    print("3) Have Ragnar calculate weight on the moon.")
    print("4) Try Ragnar's abilities by having him calculate minutes to hour(s).")
    print("5) Have Ragnar calculate Fahrenheit from Celcius.")
    print("6) See if Ragnar can multiply a word of your liking by a factor of your choice.")
    print("7) Have Ragnar print 10 numbers within a range of your choice.")
    print("8) Keep entering numbers and have Ragnar print their sum and average.")
    print("9) Let Ragnar calculate your grade by entering your score!.")
    print("10) Let Ragnar calculate the area of a circle with the radius of your choice.")
    print("11) Let Ragnar calculate the hypotenuse of a triangle with the sides of your choice.")
    print("12) Have Ragnar compare a given number to your previous number.")
    print("13) Play the guessing game with Ragnar.")
    print("14) Let Marvin print his mood.")
    print("15) Shuffle a word")
    print("16) Have Ragnar analyse a text.")
    print("17) Decrypt a file")
    print("q) Quit.")


def myNameIs():
    """
    Read the users name and say hello to Marvin.
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")


def yearsToSec():
    """
    Calculate your age (years) to seconds
    """

    years = input("How many years are you?\n")
    seconds = int(years) * (365 * 24 * 60 * 60)
    print(str(years) + " would give you " + str(seconds) + " seconds.")
    return

def weightOnMoon():
    """
    Calculate your weight on the moon
    """

    weight = input("What is your weight (in kiloes)?\n")
    moonGrav = float(weight) * .2
    print(str(weight) + " kiloes would weigh be the same as " + str(moonGrav) + " kiloes on the moon.")

def minsToHours():
    """
    Calculate hours from minutes
    """

    minutes = input("How many minutes would you want to converted to hour(s)?\n")
    hours = float(format(float(minutes) / 60, '.2f'))
    print(str(minutes) + " hours is " + str(hours) + " hours")

def celToFahr():
    """
    Calculate celcius to Fahrenheit
    """

    cel = input("Please insert Celcius to be calculated to Fahrenheit.\n")
    fah = float(format(float(cel) * 1.8 + 32, '.2f'))
    print(str(cel) + " is " + str(fah) + " in Fahrenheit units.")

def multiplyWord():
    """
    Multiply word n-times
    """

    word = input("Please enter the word.\n")
    factor = input("And please give me the product to multiply it by!")
    word *= int(factor)
    print("The word is:\n" + str(word))

def printRandNumber():
    """
    Adds 10 random numbers (depending on user range)
    to a string.
    """

    rangeMin = input("What is the lower number in your range?\n")
    rangeMax = input("What is the higher number in your range?\n")
    sequence = ""
    for num in range(0, 10):
        sequence += str(randint(int(rangeMin), int(rangeMax))) + ", "
        num = num
    print("The random sequence is:\n" + sequence[:-2])

def sumAndAverage():
    """
    Adds numbers to the sum and calculate the average value of the input(s)
    """

    summa = 0
    count = 0
    temp = input("Please enter a number to be added to the sum. \nEnter 'q' if you wish to finish!\n")
    while True:
        if temp == "q":
            print("The sum of your numbers are: " + str(summa) + "\nAnd the average is: " + str(summa/count))
            return
        else:
            try:
                summa += int(temp)
                count += 1
                temp = input("Please enter a number to be added to the sum. \nEnter 'q' if you wish to finish!\n")
            except ValueError:
                print("That's not an int! \nPlease try again!")


def gradeFromPoints():
    """
    Shows the user's grade based on his / her points
    """

    points = input("How many points did you score?\n")
    if(float(points) >= 1 and float(points) <= 100):
        points = float(points) / 100

    if float(points) >= 0.9:
        print("You got an A!")

    elif float(points) >= 0.8 and float(points) < 0.9:
        print("You got a B!")

    elif float(points) >= 0.7 and float(points) < 0.8:
        print("You got a C!")

    elif float(points) >= 0.6 and float(points) < 0.7:
        print("You got a D!")

    else:
        print("You failed the class")

def areaFromRadius():
    """
    Calculates a circles area based on it's radius
    """

    radius = input("What is the circle's radius?\n")
    area = (float(radius) * float(radius)) * 3.1416
    print("The area of the circle is: " + str(format(area, '.2f')))
    print("This was calculated with this formula: (radius^2) * 3.1416")

def calcHypotenuse():
    """
    Calculates a triangle's hypotenuse based on it's sides
    """
    side1 = input("How long is the first side?\n")
    side2 = input("How long is the second side?\n")
    hypotenuse = math.sqrt((float(side1) * float(side1)) + (float(side2) * float(side2)))
    print("The hypotenuse is: " + str(hypotenuse))

def compareNumbers(a, b):
    """
    Compares two numbers
    """
    if (a > b):
        print("Your previous number was larger!")
        return a
    elif (a < b):
        print("Your new number was larger!")
        return b
    else:
        print("They were equal!")
        return a

def validateInt(a):
    """
    Validates that an input is an integer
    """
    if a == 'q':
        return a
    else:
        flag = False
        while (flag == False):
            try:
                a = int(a)
                flag = True
            except ValueError:
                print("That's not an int! \nPlease try again!")
                a = input("Try again!\n")
    return a




def checkNumber(prev="first"):
    """
    Checks the number
    """
    print("\n=================\n")

    if prev == "first":
        prev = validateInt(input("Please input a number. Press 'q' if you wish to end\n"))
        print("\n=================\n")
        new = validateInt(input("Please input a number. Press 'q' if you wish to end\n"))
        if new == 'q' or prev == 'q':
            print("You have exited the loop\n")
            return
        else:
            compareNumbers(int(prev), int(new))
            checkNumber(str(new))
    else:
        new = validateInt(input("Please input a number. Press 'q' if you wish to end\n"))
        if new == 'q':
            print("You have exited the loop!\n")
            return
        else:
            compareNumbers(int(prev), int(new))
            checkNumber(str(new))

def guessingGame(number=0, count=0, randNumber=0):
    """
    Guessing game.
    Allows the user 6 guesses to find the right number (1-100)
    """

    if count == 0:
        randNumber = randint(1, 100)
        print("====================================================================")
        print("Welcome to the guessing game! \nIn this game you will enter a guess.")
        print("If your guess is too low / too high, Ragnar will tell you. You have 6 guesses")
        print("====================================================================")
        guessingGame(validateInt(input("What is your first guess?\n")), 1, randNumber)
    else:
        if number == randNumber:
            print("====================================================================")
            print("You guessed right! The number was: " + str(randNumber))
            print("It only took you " + str(count) + " guesses")
            print("====================================================================")
            input("\nPress enter to continue...")
        elif count == 6:
            print("====================================================================")
            print("You've had your 6 guesses.\nYou lost!")
            print("====================================================================")
            input("\nPress enter to continue...")
        elif number > randNumber:
            count += 1
            print("====================================================================")
            print("Your guess " + str(number) + " was too high. Try again!")
            print("====================================================================")
            guessingGame(validateInt(input("What is your next guess?\n")), count, randNumber)
        elif number < randNumber:
            count += 1
            print("====================================================================")
            print("Your guess " + str(number) + " was too low. Try again!")
            print("====================================================================")
            guessingGame(validateInt(input("What is your next guess?\n")), count, randNumber)

def printString():
    """
    Prints a string read from readme.txt
    """
    count = 0
    date = ""
    mood = ""
    number = ""
    realNumber = ""

    with open('readme.txt', 'r') as f:#
        for line in f:
            if count == 0:
                date += str(line)[:-1]
            elif count == 1:
                mood += str(line)[:-1].lower()
            elif count == 2:
                number += str(line)[:-1]
            elif count == 3:
                realNumber += str(line)[:-1]
            count += 1

    sentance = "Dear diary today is the {}.\nI've worked {} days straight".format(date, number)
    sentance += " and my moodpoints are {} which means I am {}...".format(realNumber, mood)
    print(sentance)
    input("\nPress enter to continue...")

def shuffleWord():
    """
    Shuffles a word of the users chosing
    """

    #importing random
    import random

    #function body
    word = input("Please enter a word to be shuffled!\n")
    print(''.join(random.sample(word, len(word))))
    input("\nPress enter to continue...")

def getQuote():
    """
    return a random quote from quotes.txt
    """
    #import random
    import random

    lines = []

    with open('quotes.txt', 'r') as f:
        sentance = f.readlines()
        lines += sentance

    print("\t\t********************** CITAT **********************\n")
    print("\t" + random.choice(lines).strip('\n'))
    print("\n\t\t********************** CITAT **********************")
    input("\nPress enter to continue....")

def doWhat(toWork):
    """
    Print from / file depending on argument
    """
    if (toWork[0:4] == "drop"):
        if (toWork[4:].strip() == ""):
            print("\nDropping all items!")
            open('inv.data', 'w').close()
            print("... done. Items dropped!")
        #open and read all files in inv.data, then close it
        f = open("inv.data", "r")
        lines = f.readlines()
        f.close()

        #re-open stream with write-priviligies
        f = open('inv.data', 'w')

        #iterate through the read lines and print all back to the file, but the dropped
        for line in lines:
            if line != toWork[5:]+"\n":
                f.write(line)
        f.close()

    elif (toWork[0:4] == "pick"):
        if sum(1 for line in open('inv.data', 'r') if line.rstrip()) <= 5:
            print("\nI already have 5 items. I can't pick anything up until I've dropped something...")
        else:
            with open("inv.data", "a") as f:
                f.write("> " + toWork[5:]+"\n")

    elif (toWork.strip() == ""):
        with open("inv.data", "r") as f:
            print("*** ITEMS ***\n")
            print('\n' .join(f.readlines()))
            print("\n*** ITEMS ***")
    else:
        print("Incorrect inventory arguments!")

    input("\nPress enter to continue...")


def analyse():
    """
    Analyses a file of the user's choice
    """
    #import listdir
    from os import listdir, path
    #import counter
    from collections import Counter
    files = "*************************************\n"
    for file in listdir():
        if file.endswith('.txt'):
            files = files + file + "\n"
    print("These are the files in your directory: \n" + files)
    choice = input("*************************************\nWhat file would you like to analyse?\n")

    if choice.strip() == "" or not path.exists(choice):
        print("No file with that name exists.\nDefaulting to alice-ch1.txt")
        choice = "alice-ch1.txt"
    elif not choice.endswith(".txt"):
        print("Adding suffix .txt")
        choice = choice + ".txt"
    else:
        print("Using " + choice)

    with open(choice) as readFile, open('common-words.txt') as common, open('words.txt') as correct:
        correct_words = correct.readlines()
        common_words = common.readlines()
        common_words = list(map(lambda s: s.strip(), common_words))
        correct_words = list(map(lambda s: s.strip(), correct_words))

        words = [word for line in readFile for word in line.split()]
        letters = [letters for letters in ''.join(words)]

        c = Counter(words)
        letterc = Counter(letters)
        counter = 0
        letterCounter = 0
        print("*************************************\nThese are the 7 most common words:")
        for word, count in c.most_common():
            if not word in common_words and word in correct_words:
                print(word + ", "  + str(count))
                counter = counter + 1
                if counter == 7:
                    break
        print("*************************************")
        print("\n*************************************\nThese are the 7 most common letters:")
        for letter, count in letterc.most_common():
            print(letter + ", " + str((count / len(letters) * 100)))
            letterCounter = letterCounter + 1
            if letterCounter == 7:
                break
        print("*************************************")
    input("\nPress enter to continue...")

LETTER_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

with open('words.txt', 'r') as low_f:
    WORDS = [word.upper().strip() for word in low_f.readlines()]

with open('common-words.txt', 'r') as high_f:
    CWORDS = [word.upper().strip() for word in high_f.readlines()]

def find_rotation(word1, word2):
    """
    Finds the rotation
    """

    rot = 0
    if word1.endswith("."):
        word1 = word1[:-1]
    if word2.endswith("."):
        word2 = word2[:-1]
    """
    HIGH PRIO
    """
    for index in range(0, len(LETTER_FREQ)):
        rot = (ord(word1[0]) - ord(LETTER_FREQ[index]))
        dec_word1 = ''.join([chr((ord(letter) - rot - 65) % 26 + 65) if (ord(letter)) >= 65 \
                            and (ord(letter)) <= 90 else letter for letter in word1])

        if dec_word1 in CWORDS:
            dec_word2 = ''.join([chr((ord(letter) - rot - 65) % 26 + 65) if (ord(letter)) >= 65 \
                                and (ord(letter)) <= 90 else letter for letter in word2])
                                
            if dec_word2 in WORDS:
                return rot
    """
    LOW PRIO
    """
    for index in range(0, len(LETTER_FREQ)):
        rot = (ord(word1[0]) - ord(LETTER_FREQ[index]))
        dec_word1 = ''.join([chr((ord(letter) - rot - 65) % 26 + 65) if (ord(letter)) >= 65 \
                            and (ord(letter)) <= 90 else letter for letter in word1])

        if dec_word1 in WORDS:
            dec_word2 = ''.join([chr((ord(letter) - rot - 65) % 26 + 65) if (ord(letter)) >= 65 \
                                and (ord(letter)) <= 90 else letter for letter in word2])

            if dec_word2 in WORDS:
                return rot

    return None

def decrypt():
    """
    decrypts the file
    """
    with open('encrypted.txt', 'r') as encrypted:
        decrypted = []
        for line in encrypted:
            line = line.split(" ")
            print(line)
            rot = find_rotation(line[0], line[1])
            for word in line:
                decrypted_word = []
                for letter in word:
                    #print(letter + ", " + str(ord(letter)))
                    if (ord(letter) > 90 or 65 > ord(letter)):
                        print(letter + ", " + str(ord(letter)) + " - becomes " + letter)
                        letter = letter
                    elif ((ord(letter) - rot) >= 65 and (ord(letter) - rot) <= 90):
                        print(letter + ", " + str(ord(letter)) + " - becomes " + chr(ord(letter) - rot))
                        letter = chr(ord(letter) - rot)
                    else:
                        print(letter + ", " + str(ord(letter)) + " - becomes " + \
                                            chr((ord(letter) - rot - 65) % 26 + 65))

                        letter = chr((ord(letter) - rot - 65) % 26 + 65)
                    decrypted_word.insert(len(decrypted_word), letter)
                decrypted.insert(len(decrypted), ''.join(decrypted_word))
        decrypted = ' '.join(decrypted)
        print(decrypted)
        input("\nPress enter to continue...")
