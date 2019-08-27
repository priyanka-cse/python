def find_devisors(n):
    lis = []
    for i in range(1,n+1):
        if n % i == 0:
            lis.append(i);
    return lis;
n = int(input("enter a number to find its devisors"))
lis1 = []
lis1 = find_devisors(n)
print(lis1)
