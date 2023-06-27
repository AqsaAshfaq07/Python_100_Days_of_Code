#!/usr/bin/env python
# coding: utf-8

# This day is about working with the conditionals. 

# In[22]:


# if-else statements 
water_level = 90
flow = 0

if water_level > 80:
    print("Drain water")
else:
    print("Continue")


# In[23]:


# Nested Conditionals - execute multiple conditons

if water_level > 80:
    if flow == 1:
        print("Drain water Quick")
    else:
        print("Take your time")
else:
    print("Continue")


# In[26]:


# Logical Operators 

if water_level > 80 and flow == 0:
    print("Drain")

if water_level > 80 or flow == 0:
    print("Drain")

if ~(water_level > 80):  # water_level < 80
    print("Continue")
      


# # Buy a Ticket

# In[38]:


# There are some prerequisites for someone to buy a ticket to ride the roller coster

height = int(input("Your height in cm: "))
age = int(input("What's your age?  "))
bill = 0
photo = input("Want photos?  Y or n")

if height >= 120:
    print("Go ahead")
    
    if age < 12:
        bill = 5
    elif age <= 18 and age >= 12:
        bill = 7
    elif age <= 55 and age >= 45:
        print("Everything is free. Have a good ride :)")
        bill = 0
    else:
        bill = 12
        
# Adding an Option of Photos
    if photo == "Y":
        print(f"Please pay ${bill + 3}")
    else:
        print(f"Please pay ${bill}")
        
else:
    print("You can't ride the roller coster")


# # Odd or Even 

# In[9]:


number = int(input("Enter a number:  "))

if number %2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# # BMI Calculator 2.0

# In[34]:


# BMI - Body Mass Index

weight = float(input("Enter your weight in kg:  "))
height = float(input("Enter your height in m:  "))
bmi = round(weight / (height*height))

if bmi < 18.5:
    print(f"Your BMI is {bmi} and You're Underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} and You have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi} and You're slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi} and You're obese")
else :
    print(f"Your BMI is {bmi} and You're clinically obese!!")


# # Leap Year

# In[39]:


year = int(input("Which year do you want to check?  "))

if year %4 == 0:
    if (year %100 != 0):
        if year %400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")


# # Pizza Order

# In[19]:


size = input("What size pizza do you want?  (S, M, L)")
pepperoni = input("Do you want to add pepperoni?  (Y, n)")
extra_cheese = input("Do you want to add extra cheese?  (Y, n)")
price = 0

if size == "S":
    price = 15
    if pepperoni == "Y":
        price += 2
    if extra_cheese == "Y":
            price += 1
    
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
            price += 1
            
elif size == "L":
    price = 25
    if pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
            price += 1
            
print(f"Please pay ${price}")


# # Love Calculator 

# In[52]:


person1 = (input("Enter your name:  ")).lower()
person2 = (input("Enter the name of your crush:  ")).lower()

names = person1 + person2

# Calculate number of times TRUE LOVE characters occur in the names
true = str(int(names.count("t")) + int(names.count("r")) + int(names.count("u")) + int(names.count("e")))
love = str(int(names.count("l")) + int(names.count("o")) + int(names.count("v")) + int(names.count("e")))

true_love = int(true + love)
true_love
# Showing use proper interpretation
if true_love < 10 or true_love > 90:
    print(f"Your love score is {true_love}, you go together like coke and mentos :)")
elif true_love < 50 and true_love > 40:
    print(f"Your love score is {true_love}, you are just right together")
else:
    print(f"Your love score is {true_love}")


# In[ ]:




