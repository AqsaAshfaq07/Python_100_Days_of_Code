# -*- coding: utf-8 -*-
"""DAY_17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zQf_SkEx0FQDidWCA-fVU_dkTo3OH4y
"""

# CLASSES
# A blueprint for creating an eventual object.

# Constructor
# A part of the blueprint that allows us to specify what'd happen when our
# object is being constructed

#  __init__
# creating Constructor function - used to initialize attributes
# it will be called everytime any new object is created from this class
# self directs to the actual object being created

class User:
  def __init__(self):
    pass  # no need to create any code inside - just pass to the next instruction

user1 = User()  # creating an object

# Names Cases

# PascalCase -> All words are capitalized
# camelCase -> All words are capitalized except the first one
# snake_case -> separating the consecutive words with underscores

# Creating attributes for that class

user1.id = 10
user1.name = "USER1"

class User:
  def __init__(self, id, username):
    self.id = id
    self.username = username

# creating an object
user1 = User(4, 'dhwo')

# accessing the attributes
print(user1.id)
print(user1.username)

class User:
  def __init__(self, id, username):
    self.id = id
    self.username = username
    self.followers = 0
    self.following = 0

  def follow(self, user):
    user.followers += 1
    self.following += 1

# creating an object
user1 = User("001", "Aqsa")
user2 = User("002", "Ayesha")

# using the method
user1.follow(user2)

# accessing the method
print(user1.following)
print(user1.followers)
print(user2.following)
print(user2.followers)
