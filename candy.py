while True:
    n=int(input())
    if n==-1:
        break
    lis=[]
    for i in range(n):
        lis.append(int(input()))
    avg=sum(lis)/n
    if avg-int(avg)!=0:
        print("-1")
    else:
        count=0
        for i in lis:
            if i>avg:
                count+=i-avg
        print(int(count))
