#!/usr/bin/env python
# coding: utf-8

# # Tuples ( )

# # create
# 

# In[18]:


t1 =() # empty typle
t1


# In[4]:


t2=(1,2,3,4,5)
t2


# In[6]:


t3=("hello",4,5,6)
t3


# In[7]:


t4= (1,2,3,(4,5))
t4


# In[13]:


# 
t5=(1)
print(type(t5))


# In[14]:


t5=("hello")
print(type(t5))


# In[15]:


# single intem of tuple create:---->

t5=("hello",)
print(type(t5))


# In[16]:


t6=tuple("goa")
t6


# In[17]:


t6=tuple([1,2,3,5,6])
t6


# In[ ]:





# #  Access

# In[19]:


t2


# In[21]:


t2[0]


# In[22]:


t2[-1]


# In[23]:


t2[:]


# In[24]:


t2[:4]


# In[25]:


t3


# In[26]:


t4


# In[27]:


t4[-1][0]


# In[ ]:





# # Edit

# In[28]:


l = [1,2,3,4,5]
l


# In[31]:


l[0]=100
l


# In[32]:


t2


# In[34]:


t2[0]=100


# # Tuples just like strings are immutable
# ## tuple creted ---> then not edited....tuple
# 

# In[ ]:





# # tuple  add ? no 

# In[35]:


t2 +t3


# In[39]:


t2 * 4


# In[40]:


for i in t2:
    print(i)


# In[42]:


i in t2


# In[43]:


len(t2)


# In[44]:


min(t2)


# In[45]:


max(t2)


# In[46]:


sum(t2)


# In[51]:


sorted(t2)


# In[57]:


sorted(t2, reverse=True)


# tupple - immultabel
# list - mutable
# 
# tupe - are read only data type
# 

# In[ ]:




