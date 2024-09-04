#  input function in python

# a = input()
# print(int(a)+int(a))
#  input function always reads input value as a string

name = input("Enter the name: ")
print(f"Welcome {name}")

age = input("Enter your age: ")
print(f"you are {age} year old !")
print(f"so next tear you will be {int(age)+1}")

#  multipal input from user -->
# input from user to add two number and print result?
x = input("Enter first number: ")
y = input("Enter second number: ")
print(f" sum of x and y is {int(x) + int(y)}")


# # hw ---> user --> input --> name,3 subject--marks 
# # print( name and precentage)??

# name = input("Enter the name: ")

# subject1 = input("Enter the first subject: ")
# subject2 = input("Enter the first subject: ")
# subject3 = input("Enter the third subject: ")

# subject1marks=input("enter the first subject Marks: ")
# subject2marks=input("enter the third subject Marks: ")
# subject3marks=input("enter the third subject Marks: ")
# # (f"\n Student name is: {name} your subject is {subject1,subject2,subject3} and your marks is {subject1,subject1marks},{subject2,subject2marks},{subject3,subject3marks}")
# print(f"\nStudent Name: {name}")
# print(f"Marks in Subject 1: {subject1  ,subject1marks}")
# print(f"Marks in Subject 2: {subject2 ,subject2marks}")
# print(f"Marks in Subject 3: {subject3  ,subject3marks}")