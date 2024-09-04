#  Operators 

# 1.Arthimetic Operators
a = 5
b = 3
print(a+b)  # addition operator
print(a-b)  # substraction operator
print(a*b)  # multiplication operator
print(a%b)  # modulus operator

#  2. Camparison operators - output is boilean value (True/False)
a=5
b=3
print(a > b) # greater then operator
print(a < b) # less then operator
c = 100
d = 100
print (c == d) # equal operator
print(a != b) # not equal operator

#  3. Assigment  operators
a = 5 # assigmant operator

# 4. logical operators
# Rule for 'and' operator
# 1. True + True = True
# 2. True + False = False
# 3. False + False = False

a = 10
b = 20
print(a > 10 and b < 10)  # and operator
print(a==10 and b==20)    
print(a==10 or b<10) # or operator

# Rule for 'or' operators
# True + False = True
print(not (a==10 and b==20))

#  5. Identity operators
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y)   # is operator
print(x is z)
print(x is not z) # is not operator

# 6. Membership Operators - in , not in
my_list = ['apple','orange','mango']
print('apple'in my_list) # in operator
print("watermelon" in my_list)

print('apple' not in my_list) # not in operator

# 7. Bitwise Operators - AND &, OR |, XOR ^, NOT ~,etc.
a = 5  # 5 in binary- 0101
b = 3  # 3 in binary- 0011
print(a & b) # 1 in binary- 0001

# Rule for '&' operator
# 1. True + True = True
# 2. True + False = False
# 3. False + False = False

print(a | b)
print(a ^ b)