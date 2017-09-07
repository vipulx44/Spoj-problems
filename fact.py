n=int(input())
for i in range(n):
    v=int(input())
    if v==0:
        print(1)
    fact=1
    for j in range(1,v+1):
        fact=fact*j
    print(fact)
