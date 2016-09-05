#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
f64a40244089e521e1cc6dda6af7ccec
python
lab1
jobk16
2016-09-03 12:03:28
v2.2.15 (2016-05-31)

Generated 2016-09-03 14:03:29 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 1 - python 
 
If you need to peek at examples or just want to know more, take a look at
the [Python manual](https://docs.python.org/3/library/index.html).

There you will find everything this lab will go through and much more.
 
"""



"""
--------------------------------------------------------------------------
Section 1. Integers, strings, floats and basic arithmetics 
 
The foundation of numbers and basic arithmetic.
 
"""

"""
Exercise 1.1 
 
Create a variable called 'numOne' and give it the value 29. Create another
variable called 'numTwo' and give it the value 71. Create a third variable
called 'result' and assign to it the sum of the first two variables.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
""" 
numOne = 29
numTwo = 71

 
ANSWER = result = numOne + numTwo  

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False)) 
"""
Exercise 1.2 
 
Create a variable called 'numThree' and give it the value 87. 

Create another variable called 'numFour' and give it the value 98. 

Subtract 'numThree' from 'numFour' and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

numThree = 87
numFour = 98

ANSWER = result = numFour - numThree  

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Find out the product of 'numOne' and 'numThree' and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
""" 

ANSWER = result = numOne * numThree

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Divide 30 with 5 and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = result = 30 / 5

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Create a variable called 'floatOne' and give it the value 15.86. 

Create another variable called 'floatTwo' and give it the value 93.49.

Sum the two values and answer with the result, rounded to 2 decimals.
 

Write your code below and put the answer into the variable ANSWER.
"""
floatOne = 15.86
floatTwo = 93.49 
ANSWER = result = float(format(floatOne + floatTwo, '.2f'))

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Subtract 'floatTwo' from 'floatOne' and answer with the result. Round to 2
decimals.
 

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = result = float(format(floatOne - floatTwo, '.2f'))

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Answer with the product of 'floatOne' and 'floatTwo', rounded to 4
decimals.
 

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = result = float(format(floatOne * floatTwo, '.4f'))

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create three variables: 'n1' = 103, 'n2' = 473 and 'n3' = 73. Sum up 'n1'
and 'n2'. Subtract 'n3' and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""
n1 = 103 
n2 = 473 
n3 = 73 
ANSWER = result = (n1 + n2) - n3

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Answer with the result of 668 modulo (%) 45.
 

Write your code below and put the answer into the variable ANSWER.
""" 

ANSWER = result = 668 % 45

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Add the word: 'syntax' to the word: 'music' and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
""" 
ANSWER = result = 'music' + 'syntax'

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Conditions, exceptions, booleans, if, else and elif 
 

 
"""



"""
Exercise 2.1 
 
Answer with the boolean value of: 400 is less than 357.
 

Write your code below and put the answer into the variable ANSWER.
"""
 
ANSWER = True if (400 < 357) else False

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Answer with the boolean value of: 53 is larger than 263.
 

Write your code below and put the answer into the variable ANSWER.
""" 
ANSWER = True if (53 > 263) else False

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Answer with the boolean value of: 400 == 53.
 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = True if (400 == 53) else False

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Create three variables representing dice values: 'd1' = 3, 'd2' = 5 and
'd3' = 3. Sum them up and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

d1 = 3
d2 = 5
d3 = 3

ANSWER = result = d1 + d2 + d3

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Create an if statement to see if the total value of your dices is 11 or
higher. If that is the case, answer with the string: 'big', else answer
with the string: 'nothing'. 
 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = "big" if(result <= 11) else "nothing"

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Create an elif statement that checks your total dice value. The checks and
results should be: three of the same value = 'triple', total of 11 or
higher = 'big', total of 10 or lower = 'small'. If you get a triple you
should not make more checks.
 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = "triple" if(d1 == d2 and d2 == d3) else "big" if ((d1 + d2 + d3) >= 11) else "small"

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Built-in functions 
 
Some useful built-in functions.
 
"""



"""
Exercise 3.1 
 
Use `max()` to find the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. 

Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = result = max(6, 8, 95, 2, 12, 152, 4, 78, 621, 45)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2 
 
Use `min()` to find the smallest number in the serie:
6,8,95,2,12,152,4,78,621,45.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = result = min(6, 8, 95, 2, 12, 152, 4, 78, 621, 45)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3 
 
Use `len()` to find the number of letters in the word: input.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = result = len('input')

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, False))

"""
Exercise 3.4 
 
Convert the number 742 to a string and add it to the word 'input'. Answer
with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = result = 'input' + str(742) 

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))

"""
Exercise 3.5 
 
Convert the number 494.87 to an integer and then to a string. Add it to the
beginning of the word: 'input'. Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = (str(int(494.87))) + 'input'

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.5", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 4. Functions 
 
Basic functions.
 
"""



"""
Exercise 4.1 
 
Create a function called 'prodNr' that takes two arguments, 54 and 96. The
function should return the product of the numbers.

Answer with a call to the function. 
 

Write your code below and put the answer into the variable ANSWER.
"""
def prodNr(arg1=54, arg2=96):
    """ docstring """
    return arg1 * arg2 
ANSWER = prodNr()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("4.1", ANSWER, False))

"""
Exercise 4.2 
 
Create a function called 'funnyWord' that takes one argument and adds it to
the string ' is a funny word'. If the argument is 'water', the function
should return: 'water is a funny word'.

Use the argument 'beverage' and answer with a call to the function.
 

Write your code below and put the answer into the variable ANSWER.
""" 
def funnyWord(inputString):
    """ docstring """
    return str(inputString) + ' is a funny word'

ANSWER = funnyWord('beverage')

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("4.2", ANSWER, False))

"""
Exercise 4.3 
 
Create a function called 'inRange' that takes one argument. The function
should return 'true' if the argument is higher than 50 and lower than 100.
If the number is out of range, the function should return 'false'. The
return type should be boolean.

Use the argument 7 and answer with a call to the function.
 

Write your code below and put the answer into the variable ANSWER.
"""
def inRange(toCheck):
    """ docstring """
    return True if(toCheck > 50 and toCheck < 100) else False

ANSWER = inRange(7)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("4.3", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 5. Iteration and loops 
 
For-loops and while-loops. 
 
"""



"""
Exercise 5.1 
 
Create a while-loop that adds 5 to the number 91, 32 times. Answer with the
result. 
 

Write your code below and put the answer into the variable ANSWER.
"""

count = 1
number = 91

while (count <= 32):
    number += 5
    count += 1


ANSWER = number

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.1", ANSWER, False))

"""
Exercise 5.2 
 
Create a while-loop that subtracts 7 from 48, 33 times. Answer with the
result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
count = 1
number = 48

while (count <= 33):
    number -= 7
    count += 1

ANSWER = number

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.2", ANSWER, False))

"""
Exercise 5.3 
 
Create a for-loop that counts the number of elements in the serie:

> 6,8,95,2,12,152,4,78,621,45

Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
count = 0
numbers = [67, 2, 12, 28, 128, 15, 90, 4, 579, 450]

for item in numbers:
    count += 1

ANSWER = count

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.3", ANSWER, False))

"""
Exercise 5.4 
 
Create a for-loop that sums up the numbers in the serie:

> 67,2,12,28,128,15,90,4,579,450

Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
result = 0
numbers = [67, 2, 12, 28, 128, 15, 90, 4, 579, 450]

for item in numbers:
    result += item

ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.4", ANSWER, False))

"""
Exercise 5.5 
 
Create a for-loop that finds the largest number in the serie:

> 6,8,95,2,12,152,4,78,621,45

Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
numbers = [6, 8, 95, 2, 12, 152, 4, 78, 621, 45]
temp_max = numbers[0]

for item in numbers:
    if(item > temp_max):
        temp_max = item


ANSWER = temp_max

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.5", ANSWER, False))

"""
Exercise 5.6 
 
Create a for-loop that goes through the numbers:

> 67,2,12,28,128,15,90,4,579,450

If the current number is even, you should add it to a variable and if the
current number is odd, you should subtract it from the variable.

Answer with the final result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
numbers = [67, 2, 12, 28, 128, 15, 90, 4, 579, 450]
result = 0

for item in numbers:
    if (item % 2 == 0):
        result += item
    else:
        result -= item


ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.6", ANSWER, False))


dbwebb.exitWithSummary()
