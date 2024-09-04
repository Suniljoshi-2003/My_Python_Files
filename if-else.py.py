#!/usr/bin/env python
# coding: utf-8

# ## 06
# 
# #  if - else Statement

# :- programing --> branching --< if-else statement

# In[10]:


# dammi email login :---->
'''
if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False
'''


# In[ ]:


# email Case condition :-
# 1.  right mail
#  2.   worng mail


# In[8]:


# correct email- campusx@gamil.com
# password - 1234

email=input ("Enter your Email: ")
password= input("Enter your Password: ")
if email == "campusx@gmail.com" and password == "1234":
    print("Welcome")
else:
    print("Incrroect credentials!!!")


# In[ ]:


# CONDITION :-
# 1.EMAIL RIGHT AND PASSWORD WORNG


# In[ ]:


email = input ("Enter the email: ")
password = input ("Enter the password: ")
if email == "campusx@gmail.com" and password == " 1234 ":
    print("WELCOME")
    
elif email == "campusx@gmail.com" and password != "1234":
    print("Incrroct password please try again !!!")
    
    password = input("Enter the password try again: ")

    if password == "1234":
        print("Finally correct")
    else:
        print("Still incrrect")
else:
    print("Incorrect credentals")


# In[5]:


# email format --> @ 


# In[6]:


email = input("Enter email")
if '@' in email:
    pass
else:
    print("Worng email")


# In[4]:


email = input ("Enter the email: ")
if '@' in email:
    password = input ("Enter the password: ")
    if email == "campusx@gmail.com" and password == " 1234 ":
        print("WELCOME")

    elif email == "campusx@gmail.com" and password != "1234":
        print("Incrroct password please try again !!!")

        password = input("Enter the password try again: ")

        if password == "1234":
            print("Finally correct")
        else:
            print("Still incrrect")
    else:
        print("Incorrect credentals")


# In[ ]:





# # indentation in python

#  if name == "xyz":
#         line1
#         line2
#         line3
# #         <---- space inditation
# else:
#     line1
#     line2
#     line3
#     

# In[10]:


name="xyz"
if name == 'xyz':
    print("line1")
    print('line2')
    if 5 == 5:
        print("line5")
    
else:
    print('line3')


# In[ ]:




