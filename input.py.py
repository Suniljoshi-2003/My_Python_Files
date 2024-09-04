#!/usr/bin/env python
# coding: utf-8

# ## 03
# 
# #  input  function

# In[1]:





# software :
#     1. static software
#     - clock,calander 
#     
#     2. dynamic software :-
#         applactions:- 
#         wabsites :-
#             : youtube, whatshapp, swaggi.

# In[2]:


# python bultaion fuction input()


# In[ ]:


input()


# In[2]:


input("Enter the Name ")


# # program

# In[6]:


#  user 2 number


# In[ ]:


first_num=input("Enter the first number: ")
secound_num=input("Enter the secound number: ")


# In[11]:


print(first_num)
print(secound_num)


# In[12]:


result= first_num + secound_num
print(result)


# INPUT FUNCTION  important proprty :
#     input function ---> use ---> input --->str (programer)

# #  type function
# :- type function use for a check the data type.

# In[15]:


print(type(result))


# In[ ]:





# # TYPE CONVERSION :-

# In[16]:


#  2 type of conversion
# 1. inplicit ----> pyhton automatically type conversion.
#  2. explicit ---> you eed to tell python  to do a type converesion at this point.


# In[17]:


#  inplicit
4 + 5.5 


# In[18]:


5 + 6+7j


# In[19]:


4.5 + 5+5j


# In[22]:


first_num + secound_num


# In[26]:


#  explicit 
int(4.5)


# In[27]:


# str 
int("44")


# In[28]:


float(4)


# In[39]:


bool(1)


# In[40]:


bool(0)


# In[41]:


complex(33)


# In[42]:


list("Hello")


# In[44]:


# int("kolkata")


# In[45]:


#  typpe conversion not parmanant operations: --->
a =3.4


# In[46]:


int(a)


# In[48]:


#  original = a
a


# In[ ]:





# # PROGRAM :) -

# In[49]:


#  USER 2 NUMBER -->


# In[5]:


first_num = int(input("ENter the first number : "))
secound_num = int(input("Enter the secound number: "))


# In[52]:


print(first_num)
print(secound_num)


# In[53]:


result = first_num + secound_num


# In[54]:


print(result)


# In[55]:


#  2nd option is :---> int 
first_num = input("ENter the first number : ")

secound_num = input("Enter the secound number: ")


print(first_num)
print(secound_num)


result = int(first_num + secound_num)


print(result)
1000


# In[4]:


x = input("Enter your name:")
print("Hello, " + x)


# In[ ]:




