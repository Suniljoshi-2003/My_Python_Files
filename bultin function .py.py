#!/usr/bin/env python
# coding: utf-8

# # 09 
# #      Bultin - in function

# # 1. print

# In[1]:


print("hello world")


# # 2. input

# In[3]:


input("enter your name : ")


# # 3. type

# In[7]:


a = 3
print(type(a))
b =5.5
print(type(b))
c= True
print(type(c))


# #  4. int etc.

# In[ ]:


# float
# str
# list
# tuple
# 


# In[10]:


int ("5")


# In[11]:


int(4.2)


# # 5. abs

# In[12]:


abs(4)


# In[13]:


abs(-4)


# # 6. pow

# In[14]:


pow(2,3)


# In[15]:


pow(2,-3)


# # 7. min / max

# In[17]:


min([2,1,3,0])


# In[18]:


max([2,4,3,6,0])


# In[20]:


min("kolkata")


# In[19]:


max("kolkata")


# # 8. round

# In[24]:


c = 22/7
print(c)
round(c)
round(c,2)


# # 9. divmod

# In[25]:


divmod(5,2)


# # 10. bin/oct/hex

# In[26]:


bin(4)


# In[27]:


oct(4)


# In[28]:


hex(4)


# # 11.id

# In[29]:


a= 13
id(a)


# In[30]:


v=22
id(v)


# # 12. ord

# In[31]:


ord('c')    
# Return the Unicode code point for a one-character strin


# In[32]:


ord("C")


# In[33]:


ord('A')


# # 13. len

# In[34]:


len("kolkata")


# In[35]:


len([1,2,3])


# # 14. sum

# In[36]:


sum([1,2,3,4,5,])


# In[37]:


sum({1,2,3,4,5})


# # 15. help

# In[38]:


#  help any function documantation read


# In[39]:


help(print)


# In[42]:


help("str")


# In[ ]:





# In[ ]:





# # Buit - in Modules in python

# <!-- what are modules -->
# Consider a module to be the same a sa code library.
# A file containing a set of functions you want to include in your application.
# Examples of python modules..
# . Math
# .Random
# . os
# . time
# 

# In[43]:


# c heck avalilable modules 
help("modules")


# In[44]:


import math


# In[45]:


math.pi


# In[47]:


math.factorial


# In[ ]:





# In[48]:


import random


# In[52]:


random.randint(1,100)


# In[55]:


a = [1,2,3,4,5]
random.shuffle(a)
a


# In[56]:


import time


# In[62]:


time.time()


# In[63]:


# current time
time.ctime()


# In[66]:


print("hello")
time.sleep(1)
print("world")


# In[67]:


import os


# In[68]:


os.getcwd()


# In[69]:


os.listdir()


# In[ ]:




