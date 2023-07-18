# -*- coding: utf-8 -*-
"""DaY_13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EU_nwbCsRagJyEXbWvmGoi90cdL0AKRL
"""

# DEBUGGING - Something which prevents code from proper functioning

# Steps and Tips to Uncover Bugs and Recover them

# 1 - Describe the Bug - Untangle the problem

def my_func():
  for i in range(1, 20):
    if i == 20:
      print("You got it!!")

my_func()

# Error here -> range function excludes the upper limit hence when i reaches 20
# the loop terminates and the print statement never gets executed!

# 2 - Reproduce the Bug

from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Now this fixes the code to print numbers from list because
# all numbers are indexed from 0-5

# 3 - Play Computer

year = int(input("What's your year of birth??"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
else:
  print("You are a human :))")

# Error here -> Every time writing a conditional --else-- is a must
# to tackle the other situations in case any occur

# 4 - Fix the Errors

age = int(input("How old are you?  "))
if age > 18:
  print(f"You can drive at age {age}.")

# Error -> f string is used without using f -- to compare age and 18, both
# should be same type -- convert input age to integer to get it compared
# to 18.

# 5 - Print is your friend :) -- helps debug code

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# 6 - Use a Debugger - python tutor

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2

  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])  # -> [26]

# Fixed Code -> using b_list.append inside the loop so it can add
# all items one by one instead of just the last one.

# 7 - Take a Break -- Stop staring at the Code :))

# 8 - Ask a Friend - a real human - a developer or some like minded people

# 9 -Run Often - execute multiple times

# 10 - Ask Stack Overflow

# Coding Exercise-1 -- Debug Even or Odd Exercise

# Code With Bugs

number = int(input("Which number do you want to check?"))

if number %2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# Fixed Code

if number %2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# Error -> Using assignment operator instead of equal check operator

# Coding Exercise-2 -- Leap Year Exercise

# Original Code
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# Fixed Code
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# Error -> leap year needs to be converted to integer first to compare
# with other intergers like here "if year % 4 == 0:"  -- year is str and
# 4 is int

# Coding Exercise-3 - Debug Fizz Buzz

# Original Code
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# Fixed Code
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

# Error - fix 'or' to 'and' -- use if-elif-else instead of using
# multiple ifs