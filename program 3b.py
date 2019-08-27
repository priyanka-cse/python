import string
import random

str1=string.printable
n=random.randint(10,15)
print(n)
print();
print(str1[random.randint(0,9)],end="")
print(str1[random.randint(10,35)],end="")
print(str1[random.randint(36,61)],end="")
print(str1[random.randint(61,93)],end="")
for i in range(n-4):
    print(str1[random.randint(0,n)],end="")

