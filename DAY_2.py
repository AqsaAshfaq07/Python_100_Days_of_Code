#!/usr/bin/env python
# coding: utf-8

# Understanding Data Types and how to manipulate Strings

# In[2]:


# using len function 
x = "12345"
len(x)  # working well with Strings


# In[4]:


# it doesn't work with integers 
y = 1243
len(y)  


# In[5]:


# It generates a TYPE_ERROR - 


# # DATA TYPES

# In[10]:


# Strings - iterables

text = "Hello"
print("Hello"[4])  # getting a single character out of the string  - Subscripting


# In[15]:


# Integers - whole numbers
x = 123,456,789
y = 123_456_789
x, y


# In[17]:


# Float - with a decimal point
x = 123.890


# In[21]:


# Boolean - two possible values
x = True
y = False
(x, y)


# In[26]:


num_char = len(input("what's your name?"))
print("Your name has " + num_char + " characters")    # -> TYPE_ERROR - can't concatanete strings with number


# In[46]:


# Solution
# 1 - Use Type Conversion
num_char = len(input("what's your name?"))
print("Your name has " + str(num_char) + " characters")   

# 2 - Use F-String
num_char = len(input("what's your name?"))
print(f"Your name has {num_char} characters")  

# 3 - Simply putting things together
num_char = len(input("what's your name?"))
print("Your name has " , num_char , " characters")


# In[34]:


# Round
x = 8/3
int(x), round(x)
 # int simply drops decimal part, round intelligently completes the number


# In[36]:


# or using 
8 // 3  # similar to int(x)


# In[44]:


# Increment Operator 
x = 4
x += 1
x = x + 1
# Both are same


# In[51]:


score = 0
height = 1.8
winning = True
print("Your score is ", score, "Your height is ", height, "Your winning chances are " , winning)

# Instead of doing this a lot of manual labor - use FString
print(f"Your score is {score} Your height is {height} Your winning chances are {winning}")


# # YOUR LIFE IN WEEKS

# In[59]:


# This challenge calculates how many weeks you're left with if you're lucky enough to live 60 years...
# Let's start by giving your age !!

age = int(input("Write your age in numbers. "))
# It would be converted to days , weeks and months
print(f"You have lived {age * 365} days, {age * 52} weeks and {age * 12} months")
total = 60 
remaining = total - age
print(f"You are left with {remaining * 365} days, {remaining * 52} weeks and {remaining * 12} months")


# # DAY_2 Project 

# Here's the link to the project of day-2 Python 100 days of code challenge.
# You can access it on replit!.
# 
# https://replit.com/@AqsaAshfaq07/tipcalculator?v=1

# # The End :)
