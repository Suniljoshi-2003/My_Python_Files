#!/usr/bin/env python
# coding: utf-8

# # Set {}

# 1. sets do not allow duplicate
# 2. sets have no indexing / slicing
# 3. sets dont allow mutable data type
# 4. set itself is a mutable data type

# # createing a set

# In[1]:


#
s1 ={}
s1


# In[2]:


type(s1)
#### worng 


# In[3]:


#  empty set create


# In[7]:


s1 = set()
s1


# In[8]:


type(s1)


# In[9]:


s1={1,2,3,4,5,6}
s1


# In[12]:


s2={"Hello",3,4.5,True}
s2


# # not allow duplicate in sets

# In[13]:


s3={1,1,2,2,3,3}
s3


# In[14]:


s4 = {[1,2,3],'Hello'}
s4 # list - mutable


# In[16]:


s4={(1,2,3),'hello'}
s4 # set - mmutable


# In[18]:


s5={{1},{2}}
s5


# #  how to access item in set

# In[19]:


s2


# In[20]:


s2[0]


# In[21]:


s2[-1]


# In[22]:


s1[0:3]


# In[23]:


# not possible


# In[ ]:





# # Edit item

# In[25]:


# NO??


# In[30]:


s1


# In[31]:


id(s1)


# In[33]:


l=list(s1)
l


# In[34]:


l[0]=100
l


# In[36]:


s1=set(l)
s1


# In[37]:


id(s1)


# In[39]:


# this id not editing
# new set create
#  sets item no access and no edit


# In[ ]:





# # sets ADD items 

# In[40]:


# yess


# In[44]:


s1
id(s1)


# In[42]:


s1.add(7)
s1


# In[43]:


id(s1)


# In[45]:


# same id add the items


# # sets iitem DELETE
# DELETE
1.DEL
2. REMOVE
3.POP
# In[49]:


del s2
s2


# In[52]:


# remove
s1


# In[56]:


s1.remove(100)
s1


# In[59]:


s1


# In[61]:


s1.pop


# In[ ]:





# # Sets operations

# In[62]:


s1 ={1,2,3,4,5}
s2={3,4,5,6,7}


# In[63]:


s1+s2
# no operaon concat


# In[65]:


s1 * 2
# no 


# In[66]:


# loop  -- yes
for i in s1:
    print(i)


# In[67]:


1 in s1


# # Function:-

# In[68]:


len(s1)


# In[69]:


min(s1)


# In[70]:


max(s1)


# In[71]:


sum(s1)


# In[72]:


sorted(s1)


# In[73]:


sorted(s1,reverse= True)


# In[74]:


# union
# all the unique number


# In[75]:


s1.union(s2)


# In[77]:


s1.intersection(s2)


# In[78]:


s1.difference(s2)


# In[80]:


s2.difference(s1)


# In[83]:


s1.symmetric_difference(s2) # vi item jo s1 and s2 main nhi h


# In[85]:


s1.isdisjoint(s2) 
# dono sets main ek bhi comman item nhi ho -->isdisjoint()


# In[86]:


s1.issubset(s2)
#  s1 ke item s2 main


# In[88]:


s1.issuperset(s2)


# In[89]:


s1.clear()


# In[90]:


s1


# In[ ]:




