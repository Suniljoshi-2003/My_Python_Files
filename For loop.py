# loops in python :-
# Loops are used to repeat instructions.
# two types of loop in python -
# 1. for loop
# 2. while loop

# 1. for loop
# basic syntex :-
# for i in varibale_name:    # i,j,k 
#     print(i)

l=[1,2,3,4,5]
for i in l:   # i=1,i=2,i=3,i=4,i=5
    print(i)   # 1 
               #
               # 5

cource=['python','java','C','C++','html','kafka','AWS','Cloud','GCP']
for my_cource in cource:
    print(my_cource)

# tuple
tup=(1,2,3,44,56,7,5,9)
for k in tup:
    print(k)

str='Python is a programing language'
for i in str:
    print(i)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# range() Function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

