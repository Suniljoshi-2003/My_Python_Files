# FUNCTIONS :
# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.


# basic syntex
def name():
    x='hello'
    print(x)
name()

# globle veriable and local veeriable

x=345644 # --> globle variable

def a():   # ----> local variabke
    d='bye'  # -----> local variabes
    print(d)
    print(x)
a()
print(x)
# print(d) #---->

def a(x,y):
    z=x*y
    print(z)
a(10,20)

