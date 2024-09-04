#!/usr/bin/env python
# coding: utf-8

# # 11
# #        List()

# # 1. what is a list 
# # 2. list vs array
# # 3. Create
# # 4. Edit
# # 5. Add
# # 6. Delete
# # 7. operations
# # 8. funcation

# In[1]:


# list - is  a data type store multipal elements.


# In[2]:


# 1.arry - homogenous (all cratears int/str)
# 2.list - hetrogenous

# 2.array contuinue memeory location data store

# 3.arrys are much faster.
#  list are more programer friendly.


# # create list

# In[7]:


l =[] # empty list
print(l)


# In[6]:


l=[1,2,3,4,5]
print(l)


# In[9]:


l2=["hello",1,3,4,True,5+0]
print(l2)


# In[10]:


#  multi-dim lists


# In[12]:


#  2D
l3=[1,2,3,[4,5]]
print(l3)


# In[15]:


#  3D
l4=[1,2,[3,4,[5,6,[7,8]]]]
print(l4)


# In[20]:


l1=[[[1,2],[3,4]],[[5.6],7,8]]
l1


# In[23]:


l5=list["hello"]
l5


# In[25]:


l5=list("hello")
l5


# In[ ]:





# # Access

# In[27]:


l2


# In[29]:


l2[0]


# In[30]:


l2[-1]


# In[31]:


l2[4]


# In[32]:


l2[1:5]


# In[33]:


l2[::-1]


# In[34]:


# 
l3


# In[35]:


l3[0]


# In[36]:


l3[-1]


# In[46]:


l3[3]


# In[49]:


l3[3][1]


# In[51]:


l3[3][:]


# In[52]:


l4


# In[60]:


l4[2][1]


# In[62]:


l1


# In[64]:


l1[1][1]


# In[78]:


l1[1][0][0]


# In[82]:


l1[1][1]


# In[83]:


l1[1][2]


# # edit

# <!-- list editing -- indexing (negtive & postative) and slysing -->

# In[91]:


l=[1,2,3,4,5]
l


# In[93]:


#  l=1 = 100
l[0]=100
l
#  List in python are Mutable???


# In[94]:


l[-1]=500
l


# In[95]:


l


# In[96]:


l[1:4]=[10,20,30,40]


# In[97]:


l


# In[ ]:





# # Add iteam in a list

# In[98]:


l


# In[99]:


#  l list end add 1000 ??


# In[100]:


l.append(1000)


# In[101]:


l


# In[102]:


#  append
#  list end add hello>
l.append("Hello")


# In[103]:


l


# In[106]:


#  extend 
#   add multipal element in the list???
l.extend([5000,6000,7000])
# append and extend list end attched element....
# append only add one element on last and
# extand multipal element add  in the list 


# In[109]:


l.append([5,6])
l


# In[112]:


l.extend("list")
l


# In[113]:


# add  the element center possation in the list??
# insert function


# In[116]:


l.insert(1,"world")
l


# In[117]:


l.insert(8,"india")


# In[118]:


l


# #  how to DELETE
# 1.  delete
# 2. del
# 3. remove
# 4. pop
# 5. clear

# In[119]:


l2


# In[120]:


del l2


# In[121]:


l2


# In[122]:


del l[0]


# In[123]:


l


# In[124]:


del l[1]


# In[125]:


l


# In[131]:


del l[-5]


# In[132]:


l


# In[133]:


del l[-8]


# In[134]:


l


# In[135]:


#  remove


# In[140]:


l.remove('goa')


# In[141]:


# pop - last element delete


# In[142]:


l.pop()


# In[143]:


l.pop()


# In[145]:


# clear - list element [] empty 


# In[146]:


l.clear()


# In[147]:


l


# # Operations

# In[149]:


l=[1,2,3,4]


# In[150]:


l1=[5,6,7,8]


# In[151]:


l + l1


# In[152]:


l


# In[153]:


l1


# In[154]:


l * 3


# In[155]:


for i in l:
    print(i)


# In[156]:


l3


# In[157]:


for i in l3:
    print(i)


# In[158]:


4 in l3


# In[159]:


3 in l3


# In[160]:


[4,5] in l3


# # Functions

# In[161]:


l


# In[162]:


len(l)


# In[163]:


min(l)


# In[164]:


max(l)


# In[165]:


sorted(l)
#  sorted is not parmanet operation


# In[166]:


sorted(l,reverse=True)


# In[167]:


l


# In[171]:


# sort
# sort is parmanant operation?


# In[172]:


l.sort()


# In[173]:


l


# In[174]:


l.sort(reverse=True)


# In[175]:


l


# In[176]:


l.sort()


# In[177]:


l


# In[178]:


l.index(3)


# In[179]:


"hello how are you".title()
# later 1st latter caps--


# In[180]:


sample="how are you?"
# sample= 'today haas been great for me'


# In[181]:


print(sample.split())


# In[184]:


# str convert 
l =[]


# In[187]:


for i in sample.split():
    print(i.capitalize())
#      caps
    l.append(i.capitalize())


# In[188]:


print(l)


# In[194]:


print(" ".join(l))


# In[193]:


#  'abc@gmail.com'
# abc
# @  sea ohlea wale alphabets
print(sample[:sample.find("@")])


# In[196]:


#  list
# [1,1,2,3,3,4,4]
# [1,2,3,4]


# In[197]:


l1=[1,1,2,2,3,3,4,4]
l2=[1,2,3,1]


# In[198]:


l =[]


# In[200]:


for i in l1:
    print(i)


# In[ ]:


for i in l1:
    if i not in l:
        l.append(i)
        

