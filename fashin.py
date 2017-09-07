n=int(input())
for i in range(n):
    num=int(input())
    a=[int(x) for x in (input().split())]
    b=[int(x) for x in (input().split())]
    a.sort()
    b.sort()
    sum=0
    for j in range(num):
        sum+=a[j]*b[j]
    print(sum)
