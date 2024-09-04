#!/usr/bin/env python
# coding: utf-8

# #                          Dicrionary {} :-

# In[3]:


#  dict = key:value pairs
#            ['name':'nitish','gender':'male']

# DICTINOARY RULES:-->
1.dict has no indexing
2.dict is a mutable data type
3. keys --> immutable, valuse ----> they can be mutable
4. keys should be unique.
# # Mutable data types ---> List/Sets/Dictionary
# 

# # Immutable data types --> String/Tuples/int/float/boolean/complex

# In[ ]:





# # create 

# In[4]:


# create empty dict


# In[5]:


D={}
D


# In[7]:


D = {'Name':'Nitish','Gender':'Male'}
D


# In[8]:


type(D)


# In[9]:


d1-{[1,2,3]:'nitish'}
d1 # list


# In[10]:


d1={(1,2,3):'nitish'}
d1  # tuple
# key immutable


# In[18]:


d2={'Name':'Rahul','Name':'Rohit'}
d2
# key-name   value update


# In[19]:


d3 ={'name':'rohit','collage':'hit','marks':{'m1':56,'ds':54,'english':55}}
d3


# In[ ]:





# # Access item from a dict

# In[20]:


d1


# In[22]:


D


# In[26]:


D[0]
# dict has no indexing


# In[27]:


#  key 

D['Name']


# In[28]:


D['Gender']


# In[30]:


d3


# In[31]:


d3['marks']


# In[33]:


#  deech marks of ds


# In[38]:


d3['marks']['ds']


# In[39]:


d3['marks']['english']


# In[48]:


#  get function
D.get('Name')


# In[ ]:





# In[ ]:





# # Edit

# In[29]:


D


# In[40]:


# change the name


# In[42]:


D['Name']='RAHUL'
D


# In[44]:


d3['marks']['ds']=65
d3


# In[ ]:





# # Add new key-value pairs

# In[49]:


D


# In[50]:


#  add age key value pair


# In[51]:


D['Age']=23


# In[52]:


D


# In[53]:


d3


# In[54]:


# add the marks 
d3['marks']['m2']=50


# In[55]:


d3


# In[ ]:





# # how to delete

# In[56]:


D


# In[65]:


del d5
d5


# In[66]:


del D ['Gender']


# In[67]:


D


# In[70]:


D.clear


# In[71]:


# operations
D


# In[72]:


d1


# In[73]:


d2


# In[74]:


d3


# In[76]:


d1+d2


# # 

# In[77]:


d1*3


# In[78]:


d3


# In[79]:


# useing loop - yes 
# output ----> retuen keys
for i in d3:
    print(i)


# In[81]:


#  loop -- key and values
for i in d3:
    print(i,d3[i])


# In[82]:


d3


# In[85]:


'rohit' in d3


# In[86]:


'name' in d3


# In[ ]:





# In[87]:


len(d3)


# In[89]:


min(d3)


# In[90]:


max(d3)


# In[91]:


sorted(d3)


# In[93]:


sorted(d3,reverse=True)


# In[94]:


d3


# In[96]:


# dict keys
d3.keys()


# In[98]:


# dict values
d3.values()


# In[ ]:




