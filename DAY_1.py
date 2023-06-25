#!/usr/bin/env python
# coding: utf-8

# # BASICS

# In[1]:


# print
print("hello world")


# In[2]:


# input 
input("Please enter your name!")


# In[3]:


# comments
#This is a comment - a non-executable code block


# In[4]:


# variable - a container to store any data 
name = 'Aqsa'


# In[5]:


# += operator 
age = 18
age += 3
# now x will be 21


# # DATA TYPES

# In[6]:


# integers - whole numbers without any decimal point
a = 1


# In[7]:


# floating point numbers - with decimal digits
pi = 3.1416


# In[8]:


# strings - series of characters or words
name = "Aqsa"


# In[9]:


# string concatenation
full_name = name + "Ashfaq"  # will become Aqsa Ashfaq


# In[10]:


# Escaping a string - to escape a "" in a string
text = "Hello, this is \"Aqsa\". "  # prints Hello, this is "Aqsa"


# In[11]:


# FStrings - insert a variable into a string
text1 = f"Hello, this is {name}"


# In[26]:


# Converting Data types
x = 9
y = 0.9
z = "9"

float(x)
int(y)
str(z)


# In[27]:


# Checking Data Types
type(x)


# # MATHS

# In[34]:


# Arithmetic Operator
5-2
5+2
5*2
5/2
5%2
5**2


# In[73]:


# Comparison Operators 
a, b = 9, 8
if a > b:
    print('yes')
    
if a < b:
    print('no')
    
if a >= b:
    print('yes')
    
if a <= b:
    print('no')
    
if a == b:
    print('yes')
    
if a != b:
    print('no')


# # ERRORS

# In[38]:


# Syntax Error - when you're not following the syntactical rules 
print(x


# In[41]:


# Name Error - using a variable before defining it, or spelling mistakes in name
print(X)


# In[43]:


# Zero Division Error
x / 0


# # FUNCTIONS

# In[45]:


# creating-calling funcions
def name(x):
    print(x)
    
name(input("enter name"))


# In[48]:


# giving an input - functions with inputs 
def solve(x, y):
    return x+y
solve(8, 9)
solve(2, 4)


# In[49]:


# functions with outputs
#  return is used to give the output of the function


# In[53]:


# Variable Scope - variables created inside function have local scope
x = 9
def add_(x, y):
    x = 0
    return x + y

add_(7, 8)  # x=0 is used in computation


# In[56]:


# keyword arguments - calling function using x or y instead of 1,2 
x = 8
y = 9
add_(x, y)


# # CONDITIONALS

# In[60]:


# if - elif - else
if name == "Aqsa":
    print(1)
elif name == "Ayesha":
    print(-1)
else:
    print(0)


# In[67]:


# compound conditions
x, y = 1, 1
if x == y and y == x:
    print('yes')
    
if x >= y or y == x:
    print('yes')
    
if ~(x!=y):
    print('yes')


# # LOOPS

# In[ ]:


# while loop - repeats until the condition returns false
a = 0
while a < 2:
    print(1)  # infinite loop


# In[1]:


# for loop - traverses all occurrences of any iterable normally
array = [1, 2, 3, 4, 5]
for _ in array:
    print(_)


# In[3]:


# break 
for i in range(3):
    if i == 3:
        break  # get out of the loop
    else:
        continue  # go to the new iteration


# # LIST METHODS

# In[9]:


# add lists together 
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr1 + arr2  # concatenates


# In[10]:


# add items to a list
arr1.append(1)
arr1


# In[12]:


# get list index
arr1[0]


# In[16]:


# list slicing - get only the specified portion of a list
arr = arr1[1:3]
arr


# # BUILT IN FUNCTIONS

# In[20]:


# range - start is included, end is not included
for i in range(6, 0, -2): # start, end, steps
    print(i)


# In[32]:


# random functions - from random library - similar to matlab
import random
random.randint(1, 4)


# In[36]:


# round
x = 9.789
round(x)

y = 9.345
round(y)


# In[38]:


# absolute value
abs(y - x)  # returns +ve value either it is negative or positive


# #    MODULES

# In[39]:


# import - preinstalled modules can be imported using import
# others need to be installed from pypi.org


# In[41]:


# aliasing - giving a short name to a module for ease of use
import random as r
r.randint(6, 90)


# In[45]:


# import from - when we need to use a part of a large module - so just import that
from sklearn.model_selection import train_test_split


# In[48]:


# import everything from a module - like importing a whole module 
from random import *


# # CLASSES AND OBJECTS

# In[50]:


# create a class
class Solution:  # naming convention - Pascal Case
    # class working code
    color = 'black'
    def add(x, y):
        
    def sub(x, y):


# In[ ]:


# create an object of a class
obj = Solution()


# In[ ]:


# class Methods
obj.add()


# In[ ]:


# class variables - they will be available to all instances of the class. 
print(obj.color)


# In[51]:


# The __init__ method - called everytime a new object is created - default class stuff is defined here that is directly accessible to all objects
# properties, variables etc


# In[53]:


# class Inheritance - a class can be inherited by another class to use its functionalities
class cls1:
    # ...

class cls2(cls1):
    #...
    
# cls2 is inheriting cls1


# # The End :)
