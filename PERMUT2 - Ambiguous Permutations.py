while True:
    n=int(input())
    if n==0:
        break
    l=[int(x) for x in input().split()]
    d={}
    flag=0
    for i in range(1,len(l)+1):
        d[i]=l[i-1]
    for i in range(1,len(l)+1):
        if l[d[i]-1]==i:
            continue
        else:
            flag=1
    if flag==1:
        print("not ambiguous")
    else:
        print("ambiguous")
