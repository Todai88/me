#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
5bc7c5fabc4542d1d4106bf59584cae5
python
lab4
jobk16
2016-09-12 12:29:26
v2.2.15 (2016-05-31)

Generated 2016-09-12 14:29:26 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 4 - python

Dictionaries and tuples.

"""



"""
--------------------------------------------------------------------------
Section 1. Dictionaries

Some basics with dictionaries.

"""



"""
Exercise 1.1

Create a small phonebook using a dictionary. Use the names as keys and
numbers as values.

Use

> Solo, Skywalker, Vader

and corresponding numbers

> 55511243, 55568711, 55590858

Add the phonenumbers as integers. Answer with the resulting dictionary.


Write your code below and put the answer into the variable ANSWER.
"""
myDict = {"Solo":55511243, "Skywalker":55568711, "Vader":55590858}
ANSWER = myDict

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

How many items are there in the dictionary?


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = len(myDict)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Use the `get()` method on your phonebook and answer with the phonenumber of
'Skywalker'.


Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = myDict.get("Skywalker")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Get all keys from the dictionary and return them in a sorted list.


Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = sorted(myDict.keys())

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Get all values from the dictionary and return them in a sorted list.


Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = sorted(myDict.values())

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Use the in-operator to test if the name 'Skywalker' exists in the
dictionary. Answer with the return boolean value.


Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = True if("Skywalker" in myDict) else False

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Use the in-operator to test if the phone number 55568711 exists in the
dictionary. Answer with the return boolean value.


Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = True if (55568711 in myDict.values()) else False

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8

Use a for-loop to walk through the dictionary and and create a string
representing it. Each name and number should be on its own row, separated
by a space. The names must come in alphabetical order.

Answer with the resulting string.


Write your code below and put the answer into the variable ANSWER.
"""

sentance = ""

for key, value in sorted(myDict.items()):
    sentance = sentance + str(key) + " " + str(value) + "\n"

ANSWER = sentance

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9

Convert the phonenumber to a string and add the prefix '+1-', representing
the language code, to each phone-number.

Answer with the resulting dictionary.


Write your code below and put the answer into the variable ANSWER.
"""
myTempDict = myDict
for key, value in sorted(myTempDict.items()):
    myTempDict[key] = '+1-' + str(value)

ANSWER = myTempDict

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10

Get and remove the item 'Skywalker' from the phonebook (use pop()). Answer
with the resulting dictionary.


Write your code below and put the answer into the variable ANSWER.
"""
myTempDict = {"Solo":55511243, "Skywalker":55568711, "Vader":55590858}

myTempDict.pop("Skywalker")

ANSWER = myTempDict

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11

Add the item you just popped from the phonebook. Answer with the resulting
dictionary.


Write your code below and put the answer into the variable ANSWER.
"""
myTempDict.update({"Skywalker":55568711})
ANSWER = myTempDict

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Tuples

Some basics with tuples.

"""



"""
Exercise 2.1

Create a tuple with 'bear, 65, 6.47, chair, 5'. Answer with the length of
the tuple as an integer.


Write your code below and put the answer into the variable ANSWER.
"""
myTuple = ('bear', 65, 6.47, 'chair', 5)
ANSWER = len(myTuple)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Create a tuple out of:

> (bear, 65, 6.47, chair, 5).

Assign each value in the tuple to different variables:

> 'a','b','c','d','e'.

Answer with the variable: 'd'. Hint: a,b,c = tuple.


Write your code below and put the answer into the variable ANSWER.
"""
(a, b, c, d, e) = myTuple

ANSWER = d

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, True))

"""
Exercise 2.3

Use the list

> [567, 23, 12, 36, 7]

Assign the first two elements to a tuple with a slice on the list.

Answer with the first element in the tuple as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

myList = [567, 23, 12, 36, 7]

myTuple = myList[:2]
a, b = myTuple

ANSWER = a

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Create a tuple with

> (elephant, 33, 7.28, stove, 4)

Convert it to a list and replace the second element with:

> "curtain"

Convert it back to a tuple and answer with the first three elements in a
comma-separated string.


Write your code below and put the answer into the variable ANSWER.
"""
myTuple = ('elephant', 33, 7.28, 'stove', 4)

myList = list(myTuple)
myList[1] = 'curtain'

myTuple = tuple(myList)
a, b, c, d, e = myTuple
print(myTuple)
ANSWER = a + "," + str(b) + "," + str(c)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))


dbwebb.exitWithSummary()
