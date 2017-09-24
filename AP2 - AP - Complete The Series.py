nofcases=int(input())
for i in range(nofcases):
    t,tl,s=[int(x) for x in input().split()]
    n=int((s/(t+tl))*2)
    diff=tl-t
    cd=diff//((n-3)-2)
    a=t-2*cd
    print(n)
    for j in range(n):
        print(a+j*cd,end=" ")
