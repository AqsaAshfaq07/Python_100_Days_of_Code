#!/usr/bin/env python
# coding: utf-8

# This day is about working with the conditionals. 

# In[14]:


# if-else statements 
water_level = 50

if water_level > 80:
    print("Drain water")
else:
    print("Continue")


# In[ ]:


# Nested Conditionals - execute multiple conditons


# # Buy a Ticket

# In[17]:


# There are some prerequisites for someone to buy a ticket to ride the roller coster

height = int(input("Your height in cm: "))
age = int(input("What's your age?  "))

if height >= 120:
    print("Go ahead")
    
    if age < 12:
        print("Please pay $5.")
    elif age <= 18 and age >= 12:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
        
else:
    print("You can't ride the roller coster")
    
    
    


# # Odd or Even 

# In[18]:


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


# In[ ]:




