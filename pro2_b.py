def rev1(str1):
    lis=str1.split(" ")
    lis.reverse()
    print(lis)
    a=" "
    s2=a.join(lis)
    print(s2)
def rev2(str1):
    lis=str1.split(" ")
    s2=""
    print(lis)
    for i in lis:
        s2+=i[::-1]
        s2+=" "
    print(s2)
str1=input("enter the string")
rev1(str1)
rev2(str1)
