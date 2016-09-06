#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
53cea6dcbabb7f8e945994764b59b3b3
python
lab3
jobk16
2016-09-06 19:37:29
v2.2.15 (2016-05-31)

Generated 2016-09-06 21:37:29 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 3 - python



"""



"""
--------------------------------------------------------------------------
Section 1. List basics



"""



"""
Exercise 1.1

Concatenate the two lists [bobcat, flute] and [Dafoe, Berenger].

Answer with your list.


Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = ["bobcat", "flute"] + ["Dafoe", "Berenger"]

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Use the list [table, wall, desk, chair, floor].

Add the words 'icecream' and 'jacket' as the second and third element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""
myList = ["table", "wall", "desk", "chair", "floor"]
myList.insert(1, "icecream")
myList.insert(2, "jacket")
ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Use the list [table, wall, desk, chair, floor].

Replace the third word with: 'light'.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""
myList = ["table", "wall", "desk", "chair", "floor"]
myList[2] = "light"

ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Sort the list

> [wasp, fly, butterfly, bumblebee, mosquito]

in ascending alphabetical order. Answer with the sorted list.


Write your code below and put the answer into the variable ANSWER.
"""


ANSWER = sorted(["wasp", "fly", "butterfly", "bumblebee", "mosquito"])

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Use the list from the last excercise

> [wasp, fly, butterfly, bumblebee, mosquito]

and sort it in decending alphabetical order. Answer with the sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = sorted(["wasp", "fly", "butterfly", "bumblebee", "mosquito"], reverse=True)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Use `pop()` to get the second and the last element in the list:

> [table, wall, desk, chair, floor]

Answer with the popped elements in a new list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["table", "wall", "desk", "chair", "floor"]
outList = [myList.pop(1)]
outList += [myList.pop()]
ANSWER = outList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Use `remove()` to delete the word:

> 'guitar'

from the list:

> [flute, guitar, drums, piano, bass]

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["flute", "guitar", "drums", "piano", "bass"]
myList.remove("guitar")

ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Built-in list functions

Some basic built-in functions.

"""



"""
Exercise 2.1

Use a built-in function to sum all numbers in the list:

> [45, 22, 2, 498, 78]

Answer with the result as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = sum([45, 22, 2, 498, 78])

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Use built-in functions, such as `sum` and `len` to get the average value of
the list:

> [67, 50, 2, 39, 15]

Answer with the result as a float with at most one decimal.


Write your code below and put the answer into the variable ANSWER.
"""
myList = [67, 50, 2, 39, 15]

ANSWER = sum(myList) / len(myList)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Use a built-in function to get the lowest number in the list:

> [123, 4, 125, 69, 155]

Answer with the result as a integer.


Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = min([123, 4, 125, 69, 155])

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Use the built-in functions `split()` and `join()` to fix this string:

> "The?grass?is?growing"

into a real sentence, (without '?').

Answer with the fixed string.


Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = " ".join("The?grass?is?growing".split("?"))

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5

Use the string:

> "For every minute you are angry you lose sixty seconds of happiness."

and split it with the delimiter " " (space).

Answer with the element at index 9.


Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "For every minute you are angry you lose sixty seconds of happiness.".split(" ").pop(9)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6

Use slice on the list

> [a, b, c, d, e]

and replace the second and third element with

> "picture, canvas"

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""
myList = ["a", "b", "c", "d", "e"]
myList[1:3] = ["picture", "canvas"]

ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
Exercise 2.7

Use slice on the list

> [a, b, c, d, e]

and replace the last two elements with

> "picture, canvas"

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["a", "b", "c", "d", "e"]
myList[-2:] = ["picture", "canvas"]



ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.7", ANSWER, False))

"""
Exercise 2.8

Use slice on the list

> [a, b, c, d, e]

and insert the words

> "picture, canvas"

after the third element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""
myList = ["a", "b", "c", "d", "e"]
temp = myList[:3] + ["picture"] + ["canvas"] + myList[3:]



ANSWER = temp

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.8", ANSWER, False))

"""
Exercise 2.9

Use `del` on the list

> [a, b, c, d, e]

and delete the first element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.9", ANSWER, False))

"""
Exercise 2.10

Use `del` on the list

> [a, b, c, d, e]

and delete the second and third element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.10", ANSWER, False))

"""
Exercise 2.11

Assign the list

> [d, c, b, a, e]

to a variable called 'list1'.

Assign the list again, but to another variable called 'list2'.

Answer with the result of 'list1 is list2'.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.11", ANSWER, False))

"""
Exercise 2.12

Use your lists from the last exercise. Assign 'list1' to another variable
called 'list3' like this:

> list3 = list1

Answer with the result of 'list1 is list3'.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.12", ANSWER, False))

"""
Exercise 2.13

Use your lists from the last exercise. Change the first element in 'list1'
to

> "x"

Answer with 'list3'.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Lists as arguments

Some excercises with passing lists as arguments to a function.

"""



"""
Exercise 3.1

Create a function that returns the list passed as argument sorted in
numerical and ascending order. Also multiply all values with 10.

Use the list:

> [123, 4, 125, 69, 155]

and the built-in method `sort()`.

Answer with the sorted list.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2

Create a function that takes the list:

> [67, 50, 2, 39, 15]

as argument.

The function should multiply all even numbers by 3 and add 9 to all odd
numbers.

Answer with the modified list sorted in numerical order, descending.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))


dbwebb.exitWithSummary()
