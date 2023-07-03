#!/usr/bin/env python
# coding: utf-8

# Randomization and Python Lists

# In[59]:


# Randomization
import random as r

random_int = r.randint(1, 100)  # includes both starting and ending numbers
print(random_int)

random_float = r.random()  # doesn't nclude starting and ending numbers 
random_float

randomFloat = r.uniform(1, 5)
randomFloat


# In[61]:


# RANDOM Module

# Creating something complicated 
# Split it into little chunks - modules 


# In[6]:


# Lists - a data structure to store large amount of data in a single place - data of different types - ordered

list_1 = [1, 2, 3, 4, 5, 6]
print(list_1)
print(list_1[0])
print(list_1[-1])


# In[13]:


# split - a string method that splits characters into a list based on some condition

s = "1 2 3 4 5 6"
s.split(" ")


# In[29]:


# List Errors

# Index out of range Error
states = ["Delaware", "Pennysylvania", "Georgia"]
len(states)

print(states[4])

# Off by 1 Error
print(states[len(states)])


# In[30]:


# Nested Lists

dirty_dozens = [["fru", "fru"], ["veg", "veg"]]  # containing lists of fruits and vegetables
dirty_dozens


# In[ ]:





# # RANDOM LOVE CALCULATOR 

# In[77]:


import random as r

name = input("Enter your name:  ")
partner = input("Enter your partner name: ")

love_score = r.randint(1, 100)
print(f"Your love score is {love_score}")


# # HEADS or TAILS

# In[76]:


import random as r

num1 = r.randint(0, 1)

if num1 == 1:
    print("Heads")
else:
    print("Tails")


# # BANKER ROULETTE

# In[26]:


import random

names = input("Enter names of all the peeps having a meal here! \n ")
names_list = names.split(" ")
n = len(names_list)

num = random.randint(0, n)
payer = names_list[num]
print(f"{payer} will pay the whole bill today!")


# # TREASURE MAP

# In[50]:


row1 = [' . ',' . ',' . ']
row2 = [' . ',' . ',' . ']
row3 = [' . ',' . ',' . ']

map = [row1, row2, row3]  # a map of blank squares  3-by-3
# print(f"{row1}\n{row2}\n{row3}")

location = input("Where do you want to put the treasure? \nEnter the row and column number")
loc_list = location.split(" ")

x = int(loc_list[0]) - 1
y = int(loc_list[1]) - 1

map[x][y] = 'X'
print(map)

