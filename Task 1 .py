#!/usr/bin/env python
# coding: utf-8

# # Python Built-in Functions 

# In[4]:


# 1 absolute function The abs() function returns the absolute value of the specified number.
# syntax abs()

abs(-7.5)


# In[1]:


# 2 bin funcion Convert an integer number to a binary string prefixed with “0b”.
# syntax bin()

bin(3)


# In[5]:


# 3 chr function Return the string representing a character whose Unicode code point is the integer i, within a valid range  
# syntax chr()

chr(97)


# In[7]:


# 4 round function Return number rounded to ndigits precision after the decimal point.
# syntax round()

round(9.378629374 , 2)


# In[10]:


# 5 min return the smallest  , max return the largest 
#syntax min() max()

numbers = [3,65,5,8,9,10,2,84]
print(min(numbers))
print(max(numbers))


# In[12]:


# 6 help funtion Invoke the built-in help system and a help page is printed on the console.
# syntax help()

help(input)


# In[28]:


# 7 zip Make an iterator that aggregates elements from each of the iterables.
# syntax zip()
names = ("Ram","Sham", "Vinod")
companies = ("Dell", "HP" , "intel")
zipped = list(zip(names,companies))
print(zipped)


# In[19]:


#8 sorted funtion Return a new sorted list from the items in iterable.
# syntax sorted()

list1 = [3,5,7,2,3,4,5,9,13,12,10,12]
sorted(list1)


# In[21]:


# 9 sum It sums a list. The list can have all types of numeric values
# syntax sum()

list2 = [3,5,2,8]
sum(list2)


# In[24]:


# 10 isinstance The isinstance(object, classinfo) function returns True if the object argument is an instance of 
#   the classinfo argument
# syntax isinstance()
numbers = [1, 2, 3, 4, 5]

isinstance(numbers, list)   

