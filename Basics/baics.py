name = "Aniket"
age = 19
weight = 51
print(name,age,weight)

# single line comment
''' 
this is a
multi -line 
comment
'''

# data types
"""
Numeric type
int - whole nums
float - decimal nums
complex - real & imaginary
"""
a = 10
b = 4.4
c = 4+4j

print(a,b,c)
print(type(a),type(b),type(c))

"""
boolean data type:
True/False
logical operations
"""

# Sequence Data types
"""
1.String -> Immutable
2.list  -> ["","",""] Mutable
3.tuple -> ("","","") Immutable
4.sets -> {...}
5.Mapping Data type
    >dictionary:pairs
"""
# operators
# Mathematical and logical symbols
# BODMAS | PEMDAS Rule

x=10
y=20
print(x+y)
print(x-y)
print(x*y)
print(x/y)  #division
print(x//y) #floor division
print(x%y)  #modulus -> remainder
print(x**y)

# comparison optr
x=10
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

# logical optr
"""
and
or
not
"""
# assignment optr
"""
=
+=
-=
*=
"""

# identity optr (used to compare memory object)
"""
is - True
is not - True

"""
a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(a is c)

# membership optr
"""
in -True
not in - True
"""
veg = ["Karela","Aloo","Tamatar"]
print("Aloo" in veg)

# control statements
"""
conditional - if,else,elif
for, while, else suite
nested
infinte loop
pass
continue
break
assert ,return

"""
# area of circle

pie = 3.147
radius = float(input("Enter radius: "))

area_of_circle = pie * radius * radius
print(f"Area of circle: {area_of_circle}")

"""

while loop

while condition:
    #code execution

-------------------------

for loop

[1,2,3,4,5]
5 times

list,tuples,dictionary,string

for variable in sequence:
    #code exec..

"""

# a = [1,2,3,4,5]
# name = "Aniket"
# for i in name:
#     print(i)

# range
"""
range(start,stop,step)
start - 1
stop - 100,exclude
step - 1
"""
a = list(range(1,11,1))
print(a)

for i in range(1,3):
    for j in range(3,6):
        print(f"{i},{j}")

# continue -> skip the current num
# break -> immediately break th loop
# pass -> dummy placeholder 

for i in range(1,11):
    if(i%2==0):
        print('even',i)
    else:
        print('odd',i)

# -------------------------------------------------

"""
string and characters

characteristics:
1.immutable
2.indexed
3.iterable
"""