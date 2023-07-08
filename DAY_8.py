#!/usr/bin/env python
# coding: utf-8

# # Functions with Inputs

# In[2]:


# Functions are code blocks written to do some functionality - they may take inputs or execute something as it is
# parameter - argument
# name - "Aqsa"


# In[8]:


# Simple Function

def greet():
    print(" Hello \n Good Morning!! \n Have a nice day :)")
    
greet()


# In[10]:


# Function getting input from user

def greet_with_name(name):  # name - input
    print(f" Hello {name} \n Good Morning!! \n Have a nice day :)")
    
greet_with_name("Aqsa")


# In[16]:


# Function with Multiple Inputs 

def greeting(name, location):
    print(f" Hello {name}, How's the weather in {location}")
    
greeting("Aqsa", "Pakistan")
    


# In[21]:


# def addition(a, b, args):
#     print(a + b + args)
    
# addition(1,2,3,4,5,6)


# In[24]:


#  Function with keyword Arguments - takes predefined args if they're not provided by user - else prints the user givena args

def keyword_args(name = "Aqsa", location = "xyz"):
    print(f"Hello {name} from {location}")
    
keyword_args("james")


# # AREA CALCULATION

# In[33]:


# Given the height and width of a wall, calculate no. of cans required to paint the whole area

height_ = int(input("Enter height of the wall:  "))
width_ = int(input("Enter width of the wall:  "))

def cans_of_paint(height, width):
    no_of_cans = round((height * width) / 5)
    print(f"You need to buy {no_of_cans} cans of paint")

cans_of_paint(height_, width_)


# # PRIME NUMBER CHECKER

# In[39]:


# prime number - that can only be divided by itself

n = int(input("Check this number:  \n"))

def prime_checker(number):
    if number%2 != 0 and number%3 != 0 and number%5 != 0:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

prime_checker(n)


# # CAESAR CIPHER

# In[85]:


# Encode and decode text for better security 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
          'x', 'y', 'z']


# In[107]:


# Step - 1

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:  \n")
message = input("Type your message:  \n")
shift = int(input("Type the shift number:  \n"))


# In[103]:


# Step - 2 - now encode the message

def encrypt(message_, shift_):
    cipher_text = ""
    for char in message_:
        pos = letters.index(char)
        new_pos = pos + shift_
        
        if new_pos >= 26:
            new_pos -= 26 
            
        new_char = letters[new_pos]
        cipher_text += new_char
    print(f" The encrypted text is {cipher_text}")
    
encrypt(message, shift)


# In[106]:


# Step - 3 - now decrypt the message 

def decrypt(message_, shift_):
    decrypted_text = ""
    for char in message_:
        pos = letters.index(char)
        new_pos = pos - shift_
        new_char = letters[new_pos]
        decrypted_text += new_char
    print(f" The decrypted text is {decrypted_text}")
    
decrypt(message, shift)


# In[ ]:


# Step - 4 - taking decisions

if direction == "encrode":
    encrypt(message, shift)
elif direction == "decode":
    decrypt(message, shift)


# In[114]:


# COMPLETE SOLUTION


# In[123]:


# Encode and decode text for better security 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
          'x', 'y', 'z']

# Step - 1

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:  \n")
message = input("Type your message:  \n")
shift = int(input("Type the shift number:  \n"))


# Step - 2 - taking decisions

if direction == "encode":
    encrypt(message, shift)
elif direction == "decode":
    decrypt(message, shift)
else:
    print("Please enter correct operation to be performed!")

# Step - 3 - now encode the message

def encrypt(message_, shift_):
    cipher_text = ""
    for char in message_:
        pos = letters.index(char)
        new_pos = pos + shift_
        
        if new_pos >= 26:
            new_pos -= 26 
            
        new_char = letters[new_pos]
        cipher_text += new_char
    print(f" The encrypted text is {cipher_text}")
    
# encrypt(message, shift)

# Step - 4 - now decrypt the message 

def decrypt(message_, shift_):
    decrypted_text = ""
    for char in message_:
        pos = letters.index(char)
        new_pos = pos - shift_
        new_char = letters[new_pos]
        decrypted_text += new_char
    print(f" The decrypted text is {decrypted_text}")
    
# decrypt(message, shift)


# In[124]:


# BETTER SOLUTION - LESS REDUNDANCY


# In[4]:


# Encode and decode text for better security 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
          'x', 'y', 'z']


# Step - 2 - Use just caesar function

def caesar(direction_, message_, shift_):
    cipher_text = ""
    
    for char in message_:
        if char in letters:
            pos = letters.index(char)
            if direction == "encode":
                new_pos = pos + (shift_ % 26)  # shift_ % 26 -> to tackle with higher shift numbers 
            else:
                new_pos = pos - (shift_ % 26)
            if new_pos >= 26:
                new_pos -= 26 
            new_char = letters[new_pos]
            cipher_text += new_char
            
        else:  # to tackle with number/symbols/spaces
            cipher_text += char

    print(f"The cipher text is {cipher_text}")
    

# Step - 1

continue_ = True

while continue_:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:  \n")
    message = input("Type your message:  \n")
    shift = int(input("Type the shift number:  \n"))
    caesar(direction, message, shift)
    
    result = input("Type 'yes' if you want to continue, otherwise type 'no'")
    if result == "no":
        continue_ = False
        print("Good Bye :)")


# In[127]:


# IMPROVING USER EXPERIENCES


# In[ ]:




