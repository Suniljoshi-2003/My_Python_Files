#!/usr/bin/env python
# coding: utf-8

# # FUNCTIONS

# In Python, a function is a reusable block of code that performs a specific task. Functions allow you to organize your code into modular pieces that can be easily reused, making your code more manageable, readable, and efficient.

# # Components of a Function

# In[2]:


def  is_even(i):
    """
    function info?
    """
    x = i % 2 == 0
    return x
is_even(7)


# '''
# # def function info -->
# 
# def --> keyword
# is_even ----> name 
# (i): ----> pracmeters or arguments
#     '''
#     input: ia s posotive int retusrns true if i is even, otherwise false
#     '''
#     
#     
#     print -----> ("inside is_even")
#                                       ----> body
#     return i %  2 == 0
# 
# is_even(3)  ----------------> function calling\
# '''

# In[ ]:





# In[20]:


def is_even(number):
    '''
    this function tells if a given number is odd or even
    input - any valud integer
    output - even / odd
    Created by - SUNIL
    last edited - 09 AUGUST 2024
    '''
    
    if number % 2 == 0:
        return 'Even'
    else:
        return'Odd'
print()
    
    


# In[21]:


for i in range(1,11):
    print(is_even(i))


# In[22]:


#  function doc. chek syntex......

print(is_even.__doc__)


# In[23]:


print.__doc__


# In[24]:


type.__doc__


# In[57]:


def is_even(number):
    if type(number) == int:
       
        if number % 2==0:
            return 'Even'
        else:
            return 'Odd'
       
    else:
        return 'Not allow'
print()


# In[37]:


is_even('hello')


# In[38]:


is_even(101)


# In[39]:


is_even(222)


# In[59]:


is_even(34)


# In[ ]:





# # Parameters VS Arguments
# 1. Default arguments
# 2. Positional argument 
# 3. keyword arguments
# 4. Arbitrary arguments

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[32]:


def power(a,b):
    return a**b
print()


# In[36]:


power(2,3)


# In[61]:


power(3,7)


# In[62]:


power(3)


# In[67]:


# code creesh
#  the right way of code


# In[68]:


def power(a=1,b=1):
    return a**b


# In[69]:


power(2,3)


# In[70]:


power(3)


# In[71]:


power()


# In[72]:


power(2,3)
#  positional argument


# In[74]:


power(b=2,a=3)
# keyword argument


# In[ ]:





# In[77]:


def flexi(*number):
    product = 1
    print(number)
    print(type(number))
    for i in number:
        product = product * i
    print(product)


# In[78]:


flexi(1,2)


# In[80]:


flexi(1,2,3,4,5,6)


# In[81]:


def greet(name="Guest"):
    return f"Hello, {name}!"


# In[83]:


greet("sunil")


# In[85]:


greet ("manish")


# In[86]:


def multiply(x, y):
    return x * y


# In[87]:


multiply(3,5)


# In[88]:


def square(number):
    return number ** 2


# In[89]:


square(88)


# In[96]:


square(44)


# In[98]:


def build_profile(first, last, **user_info):
    profile = {
        'first_name': first,
        'last_name': last,
    }
    profile.update(user_info)
    return profile


# In[100]:


user_profile = build_profile('John', 'Doe', location='New York', field='Engineering')
print(user_profile)


# In[103]:


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# In[105]:


factorial(9)


# In[107]:


factorial(3)


# In[ ]:





# In[ ]:





# In[1]:


# Functions as Object
def f(num):
    return num ** 2


# In[2]:


f(2)


# In[3]:


f(4)


# In[4]:


x=f


# In[5]:


x(2)


# In[6]:


x(6)


# In[8]:


del f


# In[10]:


f()


# In[11]:


x(2)


# In[12]:


type(x)


# In[13]:


l=[1,2,3,4]


# In[14]:


l


# In[15]:


l=[1,2,3,4,x]


# In[16]:


l


# In[17]:


l[-1](3)


# In[19]:


l=[1,2,3,4,x(5)]
l


# In[20]:


#  renameing a fnction
# deleting a function
# storing a function
# function as argument


# In[ ]:


#  benefits of using a function
# code modularity
# code reusability
# code readbility

