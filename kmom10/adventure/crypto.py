"""
Crypto class.
"""

LETTER_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

with open('words.txt', 'r') as low_f:
    WORDS = [word.upper().strip() for word in low_f.readlines()]

with open('common-words.txt', 'r') as high_f:
    CWORDS = [word.upper().strip() for word in high_f.readlines()]


INSTRUCTIONS = """
################### INSTRUKTIONER ##############################
###
###  Du kommer få tre krypterade meningar som du ska dekryptera.
###  Det FÖRSTA ordet i meningen ska DU försöka knäcka.
###  Resten av orden kommer lösas av Ragnar.
###  Om du inte kan gissa dig till ordet så kan du skriva 'LÖS'.
###  Detta låter Ragnar lösa hela meningen.
###  Oroa dig inte. Du får tillgång till rummet oavsett! :)
###
################################################################
"""

def cls():
    """
    Rensar konsolen för att ge lättare data.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def init_crypto():
    """
    Startar loopen.
    """
    decrypt()

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

        for line in encrypted:
            decrypted = []
            line = line.split(" ")
            sentance = line
            rot = find_rotation(line[0], line[1])
            for word in line:
                decrypted_word = []
                for letter in word:
                    #print(letter + ", " + str(ord(letter)))
                    if (ord(letter) > 90 or 65 > ord(letter)):
                        letter = letter
                    elif ((ord(letter) - rot) >= 65 and (ord(letter) - rot) <= 90):
                        letter = chr(ord(letter) - rot)
                    else:
                        letter = chr((ord(letter) - rot - 65) % 26 + 65)
                    decrypted_word.insert(len(decrypted_word), letter)
                decrypted.insert(len(decrypted), ''.join(decrypted_word))
            print_info(sentance)
            get_in(decrypted)
        decrypted = ' '.join(decrypted)


def get_in(decrypted):
    """
    Tar spelarens input för att se utifall han löst
    dekrypteringen av första ordet i meningen.
    """
    done = False

    while done == False:
        guess = input("Vad är ditt val? Tänk på att du har meningen,"\
              " men du ska 'bara' översätta FÖRSTA ordet!\n")

        if guess.upper() == decrypted[0]:
            print("Du löste dekrypteringen!")
            done = True
        elif guess.upper() == "LÖS":
            print("Ragnar löser detta åt dig. Rätt ord var: " + decrypted[0])
            done = True
        else:
            print("Felaktigt val! Pröva igen. Tänk på att du kan använda 'LÖS' "\
                   "för att låta Ragnar lösa dekrypteringen för dig!")
    print("\n################# DEKRYPTERAD #######################\n")
    print("\t\t" +' '.join(decrypted).strip())
    print("\n#################  MENING  ##########################\n")
    input("Tryck på en tangent för att fortsätta!")

def print_info(sentance):
    """
    Skriver ut instruktioner och ord, meningen som han ska översätta.
    """
    cls()
    print(INSTRUCTIONS)
    mening = """\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        MENING:   {}
        ORD:      {}

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """.format(' '.join(sentance),\
            sentance[0])
    print(mening)
