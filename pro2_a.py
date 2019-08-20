def Search(lis,key):
    print(lis)
    if key in lis:
        return True
    else:
        return False
lis=[]
while True:
    a=int(input("enter the element"))
    if a != -1:
        lis.append(a)
    else:
        break
key=int(input("enter the element to be searched"))
xx = Search(lis,key)
if xx==True:
    print("key found")
else:
    print("key not found")
