"""
This is the main python class.
"""
#!/usr/bin/env python3
from marvin import menu, myNameIs, yearsToSec, weightOnMoon, minsToHours, celToFahr, multiplyWord, printRandNumber
from marvin import sumAndAverage, gradeFromPoints, areaFromRadius, calcHypotenuse, checkNumber
from marvin import guessingGame, printString, shuffleWord

def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    while True:
        menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return

        elif choice == "1":
            myNameIs()

        elif choice == "2":
            yearsToSec()

        elif choice == "3":
            weightOnMoon()

        elif choice == "4":
            minsToHours()

        elif choice == "5":
            celToFahr()

        elif choice == "6":
            multiplyWord()

        elif choice == "7":
            printRandNumber()

        elif choice == "8":
            sumAndAverage()

        elif choice == "9":
            gradeFromPoints()

        elif choice == "10":
            areaFromRadius()

        elif choice == "11":
            calcHypotenuse()

        elif choice == "12":
            checkNumber()
        elif choice == "13":
            guessingGame()
        elif choice == "14":
            printString()
        elif choice == "15":
            shuffleWord()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

            input("\nPress enter to continue...")



if __name__ == "__main__":
    main()
