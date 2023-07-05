#!/usr/bin/env python
# coding: utf-8

# # Python Loops

# In[6]:


fruits = ['apple', 'peach', 'pear']
for fruit in fruits :
    print(fruit)
    print(fruit + " Pie")
    # print(fruits)  # gets printed everytime for loop is executed

print(fruits)   # gets printed just after the loop terminates


# In[37]:


# Range Function - iterates over the given numbers or lists 
sum_ = 0

for number in range(1, 101):  # second number isn't included
    sum_ += number
    
print(sum_)


# # AVERAGE HEIGHT 

# In[21]:


#  Complete the challenge without using len() and sum()

student_heights = input("Input a list of student heights. \n").split()
total_height = 0
items = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_height += student_heights[n]
    items += 1
    
average = total_height / items
print(average)


# # HIGHEST SCORE

# In[30]:


student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = student_scores[0]

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")


# # ADDING EVENS

# In[45]:


# Calculate sum of all even numbers from 1-100 inclusive.

even_sum = 0
for num in range(2, 101, 2):
    even_sum += num
    
print(even_sum)

# OR

total = 0
for num in range(2, 101):
    if num %2 == 0:
        total += num
        
print(total)


# # FIZZ BUZZ

# In[49]:


print("Welcome to the FizzBuzz Game!")

for num in range(1, 101):
    if (num %3 == 0) and (num %5 == 0):
        print("FizzBuzz")
    elif num %3 == 0:
        print("Fizz")
    elif num %5 == 0:
        print("Buzz")
    else:
        print(num)

