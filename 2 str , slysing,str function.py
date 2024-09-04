#!/usr/bin/env python
# coding: utf-8

# # 
# #            Indexing

# In[1]:


# concept of indexing
#  indexing start --> 0


# In[2]:


c= "hello"
print(c)


# In[3]:


print(c[0])


# In[4]:


print([2])


# In[5]:


#  types of indexing 
#  1. positive indexing --> left  to right
#  2. negative indexinf ---> right to left


# In[6]:


# positive indexing


# In[7]:


x="hello"
print(x[0])


# In[8]:


print(x[4])


# In[9]:


# negative indexing


# In[10]:


x="hello"


# In[11]:


print(x[-1])


# In[13]:


print(x[-3])


# In[ ]:





# # Slicing

# In[14]:


# slicing :
c="hello world"
print(c)
# feetch the hello?


# In[16]:


print(c[0:5])


# In[18]:


print(c[0:])


# In[19]:


print(c[:])


# In[20]:


print(c[1:])


# In[26]:


print(x[:-4])


# In[27]:


print(c[:5])


# In[28]:


# stsrt : stop : steep


# In[30]:


print(c[0:7:2])


# In[34]:


print(x[0:8:3])


# In[38]:


print(c[0:6:-1])
# no result


# In[39]:


print(c[-5:-1:2])


# In[48]:


print(x[::-1]) # str revrese


# In[50]:


print(c[-1:-5:-1])


# In[ ]:





# #  Editing and Deleting in string

# In[ ]:





# In[51]:


c= "Hello"
print(c)


# In[52]:


# H --> X


# In[54]:


# c[0]='X' 
#  strig are a inmutable Data type


# In[56]:


c = "world"
print(c)


# In[57]:


#  Deletion


# In[58]:


del c


# In[60]:


print(c)


# In[62]:


c= 'Hello'
print(c)


# In[64]:


# del c[0]str' object doesn't support item deletion


# In[ ]:





# #  operstions on String

# In[65]:


#  arithmetic op


# In[66]:


"Hello" + " world"


# In[67]:


"Hello" + "-" + "World"


# In[68]:


print("*"*50)


# In[69]:


print("Hello"*4)


# In[70]:


"hello" == "world"


# In[71]:


"hello" == "hello"


# In[72]:


"hello" != "world"


# In[74]:


"mumbai" > "pune"
# Lexiographically


# In[76]:


"goa"< "kolkata"


# In[77]:


"KOl" < "kol"


# In[78]:


"Hello" and "world"


# In[80]:


# ""-> Flase
# "wreghr" -> True


# In[81]:


"" and "Hello"


# In[82]:


"" or "wolrd"


# In[83]:


"hello" or "world"


# In[84]:


"hello" and "world"


# In[85]:


not "hello"


# In[86]:


not""


# In[88]:


c ="hello world"
for i in c:
    print(i)


# In[94]:


c="hello world"
for i in c[::]:
    print(i)


# In[100]:


c="hello world"
for i in c[2:15:2]:
    print(i)


# In[ ]:





# In[101]:


c


# In[103]:


"h" in c


# In[104]:


"H" in c


# In[105]:


'world' not in c


# In[ ]:





# #  String Functions
1.len
 2.   max
   3.   min
      4.  sorted
# In[107]:


x="kolkata"
print(len(x))


# In[108]:


max(x)


# In[109]:


min(x)


# In[110]:


sorted(x)


# In[112]:


sorted(x,reverse=True)


# In[ ]:





# # 1. Capitalize / Title / Upper / Lower / Swapcase

# In[113]:


x


# In[116]:


x.capitalize() # first alphabets latter caps.


# In[118]:


"It is raninig today".title() 
#  alphabets first latter is  caps


# In[120]:


c.upper() 
# upper ---  all alphabets captial


# In[123]:


c.lower()
# lower all alphabets lower case


# In[125]:


"Kolkata".swapcase() 
# caps later -- small and samll later cpas


# # 2. count

# In[126]:


"It Is raining".count("i")


# In[127]:


"It Is raining".count("n")


# # 3. filnd / index

# In[129]:


"It Is raining".find("i")
# posation


# In[130]:


"It Is raining".find("r")


# In[132]:


"It Is raining".find("z")
#  z is not present in th str and ans -1


# In[133]:


#  index


# In[135]:


"It Is raining".index("rain")


# In[136]:


#  find and index 
# find -1 return
# index error


# # 4. endswith / startwith

# In[137]:


"it is raninng today".endswith("y")


# In[138]:


"it is raninng today".endswith("t")


# In[139]:


"it is raninng today".endswith("day")


# In[145]:


"it is raninng today".startswith("d")


# In[144]:


"it is raninng today".startswith("it")


# # 5. fromat

# In[148]:


"Hello my name is {} and i am {}".format("Nitish",22)


# In[150]:


# posation
"Hello my name is {1} and i am {0}".format("Nitish",22)


# In[154]:


"Hello my name is {name} and i am {age}".format(name="Nitish",age=22)


# # 6. isalnum / isalpha / isdecimal / isdigit / isidentifire

# In[156]:


# isalnum - check the string alphabets and numbbers.
"FLAT20".isalnum()


# In[157]:


'flat20@#$'.isalnum()


# In[158]:


# isalpha - present on alphabets
'asdfghj'.isalpha()


# In[160]:


"123@4n".isalpha()


# In[161]:


# isdigit - number check 
"2345678".isdigit()


# In[162]:


"jh5678".isdigit()


# In[167]:


"Hello_world".isidentifier()


# In[168]:


"w g".isidentifier()


# # 7. split

# In[171]:


# split - string convert on list
"wo is the pm of india".split()


# In[172]:


"wo is the pm of india".split("is")


# In[173]:


"wo is the pm of india".split("x")


# # 8. join

# In[174]:


"-".join(['wo', 'is', 'the', 'pm', 'of', 'india'])


# In[175]:


"@".join(['wo', 'is', 'the', 'pm', 'of', 'india'])


# # 9.Replace

# In[176]:


"Hi my name is Nitish".replace("Nitish","Mahima")


# # 10. strip

# In[184]:


name = "       nitish       "
print(name)
"hii"+name + "how are you"


# In[185]:


#  strip  = remove on spaces
name.strip()


# In[ ]:




