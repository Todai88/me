#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
18611c57693f3281c28eaeb45e40cdf7
python
lab2
jobk16
2016-09-04 08:24:51
v2.2.15 (2016-05-31)

Generated 2016-09-04 10:24:52 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 2 - python 
 
Strings and files.
 
"""



"""
--------------------------------------------------------------------------
Section 1. Strings 
 
The basics of strings.
 
"""



"""
Exercise 1.1 
 
Assign the word: 'cupcakes' to a variable and put your variable as the
answer.
 

Write your code below and put the answer into the variable ANSWER.
"""
placeholder = "cupcakes"

ANSWER = placeholder

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Assign the word 'cupcakes' to a variable. Create another variable where you
put the first and the last letter in the word.

Answer with the second variable.
 

Write your code below and put the answer into the variable ANSWER.
"""

firstAndLast = placeholder[0:1] + placeholder[-1] 
ANSWER = firstAndLast
# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Assign the word: onion to a variable. Answer with the length of the word as
an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""
word = "onion"
number = len(word)

ANSWER = number
# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Use the 'in-operator' to see if the word: 'cabbage' contains the letter
'a'. Answer with a boolean result.
 

Write your code below and put the answer into the variable ANSWER.
"""
flag = False

if "a" in "cabbage":
    flag = True


ANSWER = flag

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Make all the letters in the word 'onion' capitalized. Answer with the
capitalized word.
 

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "onion".upper()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use the built-in function `startswith()` to see if the word 'onion' starts
with the letter 'o'. Answer with the boolean value.
 

Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = True if "onion".startswith("o") else False

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Assign the words: 'lollipop' and 'lemon' to two different variables. 

Create a function and pass the two words as arguments to it. Your function
should return them as a single word.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""
def concat(a, b):
    """
    Concats two strings
    """
    return (a + b)

word1 = "lollipop"
word2 = "lemon"


ANSWER = concat(word1, word2)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create a function and pass the word: 'cupcakes' to it. Your function should
return the sentence:

> "This word was: cupcakes"

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

def printSentance(a):
    """
    Returns an arbitrary sentance to be printed
    """
    return "This word was: " + a




ANSWER = printSentance("cupcakes")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Create a function and pass the word: 'lemon' to it.

Your function should return the string 'yes' if the word is longer than 5
characters. Else return 'no'.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""
def returnLenght(a):
    """
    Returns the length of a word
    """
    return "yes" if (len(a) > 5) else "no"





ANSWER = returnLenght("lemon")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Create a function and pass the word: 'onion' to it.

Your function should return a string with the word backwards.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

def reverseWord(a):
    """
    Reverses a word
    """
    return a[::-1]

ANSWER = reverseWord("onion")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11 
 
Create a function and pass the word: 'lollipop' to it.

Your function should exclude the first and the last letter of the word and
return it.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""
def sliceFaL(a):
    """
    Returns the string with First and 
    Last letter sliced
    """
    return a[1:-1]





ANSWER = sliceFaL("lollipop")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
Exercise 1.12 
 
Use `str.format()` to print out:

> 'My 'string' has 'integer' 'string''.

Use the values: 'book', '398' and 'pages'. Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "My {} has {} {}".format("book", 398, "pages")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.12", ANSWER, False))

"""
Exercise 1.13 
 
Use `find` and `slice` on the string:

> "196.98.2.54 : (tree), window"

to get the word inside the parenthesis.

Answer with the word as a string.
 

Write your code below and put the answer into the variable ANSWER.
"""
sentance = "196.98.2.54 : (tree), window"
fParant = sentance.find('(') + 1
sParant = sentance.find(')')

ANSWER = sentance[fParant:sParant]

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Files 
 
This section uses the text file: '[httpd-access.txt](httpd-access.txt)'.
 
"""



"""
Exercise 2.1 
 
Open the file and count the number of times a line starts with '81'. Answer
with the result as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""
count = 0
with open('httpd-access.txt', 'r') as f:
    for line in f:
        if "81" in line[0:2]:
            count += 1
 
ANSWER = count

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Find out the last 4 digits on line 821 in the file. Answer with the result
as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""
count = 0
with open('httpd-access.txt', 'r') as f:
    for line in f:
        count += 1
        if count == 821:
            s = line[-5:-1]

ANSWER = int(s)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Find out which of the ip adresses 81.226.253.26 and 95.19.133.73 that has
the highest amount of entries in the file.

Answer with the result as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""
fCounter = 0
sCounter = 0

with open('httpd-access.txt', 'r') as f:
    for line in f:
        if line[0:13] == "81.226.253.26":
            fCounter += 1
        elif line[0:12] == "95.19.133.73":
            sCounter += 1






ANSWER = fCounter if(fCounter > sCounter) else sCounter

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Count the number of periods (.) there are in the file.

Use the built-in function `count()` on the file after you have converted it
to a string.

Answer with the result as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""
s = ""
with open('httpd-access.txt', 'r') as f:
    for line in f:
        s += line

ANSWER = s.count('.')

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Find the characters on line 637 from index 65 to index 75. Make sure that
the character at index 75 also gets included.

Answer with the piece of string you found.
 

Write your code below and put the answer into the variable ANSWER.
"""
s = ""
count = 0

with open('httpd-access.txt', 'r') as f:
    for line in f:
        count += 1
        if count == 637:
            s = line[65:76]

ANSWER = s

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Find the last element (digit) on each line, if there are any, and sum all
that are even.

Answer with the result as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""
result = 0

with open('httpd-access.txt', 'r') as f:
    for line in f:
        try:
            if int(line[-2:-1]) % 2 == 0:
                result += int(line[-2:-1])

        except ValueError:
            incorrectBuffer = line[-2:-1]

ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))


dbwebb.exitWithSummary()
