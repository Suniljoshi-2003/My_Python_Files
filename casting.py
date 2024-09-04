#  casting in python

a = 6
print(type(a))  # int

b = '2'
print(type(b))  # str
# print(a+b)

c = int(b)
print(type(c))

print(a + c)
print(a + int(b))

# all str tye can't be cast into numerical type
name ="Madhav"
# newname = int(name) 

#  all numerical type can be cast into str
mynum = 26
mynum2 = str(mynum)
print(type(mynum2))

f1 = 22.34
f2 = int(f1)
print(type(f1))

in1 = 65
print(type(float(in1)))

#  implicit type casting
var1 = 10
var2 = 15.11
var3 = var1 + var2
print(var3)
print(type(var3))

#  Explcit type casting
int_num = 101
str_num = str(int_num)
print(type(int_num))

# bool --> True/1 and False/0
a0 = bool(0)
a1 = bool(1)
print(a0)
print(a1)
print(type(a0))
print(type(a1))