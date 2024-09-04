#  Data Types in Python
a = 1
b = 1
# print(a)
print(a+b)
print(type(a)) # checking dat type : integer

c = '1'
d = '1'
print(c+d)
print(type(c)) # checking data type: string

#  Basic data types in Pyhton
# 1. Numeric
a1 = 1     # 1a. integer
a2 = 2.3   # 1b. float
print(type(a1))
print(type(a2))

a3 =complex(3,5)  #1c. compex
print(type(a3))

# 2. Sequence
b1 = "Sunil"   # 2a. string
print(type(b1))

b2 =[1,2,"Absdefg",3,4,65,64,100] #2b. list
print(type(b2))

b3 = (1,22,445,"Sunil",765) # 2c. tuple
print(type(b3))

#  Dictionary
my_dictionary = {'name': 'Sunil',
                 'age':21,
                 'study':'pyhton programing',
                 'city':'Uttarakhand'}
print(type(my_dictionary))

# 4. Sets
my_sets = {1,22,445,"Sunil",765}
print(type(my_sets))

#  5. Boolean
bool1 = True
bool2 = False
print(type(bool1))
print(type(bool2))

# 6. Binary
# bytes . bytearray , memoryview
byte1 = b"sunil"
print(type(byte1))
