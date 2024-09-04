# Assignment - 2
# Q1: Write a Python program to input student name and 
# marks of 3 subject. print name & percentage in output?

# optimized solution
print("Percentage Calculator")
student_name = input("Enter your name: ")
hindi_marks = int(input("Enter Hindi Marks: "))
maths_marks = int(input("Enter Maths Marks: "))
science_marks = int(input("Enter the Science Marks: "))
 
#  calcualating percentage
percentage = ((hindi_marks)+ (maths_marks) + (science_marks)/300)*100

# print result
print(f"The result of {student_name}is {int(percentage)}%. Well done!")

# 
# Q2: Write a Python program that collects multiple types of data 
# (e.g., name, age, height and student status)
# from user input,stores them in a dictionary and then
# prints out the collected data?

# initializing a dictionary
user_data ={}

#  input from user
user_data ['name'] = input("Enter your name: ")
user_data ['age'] = int( input("Enter your age: "))
user_data ['height'] = float(input("Enter your height: "))
user_data ['student'] = input("Are you a student(yes/no) ")

# print the input from user
print(user_data)


