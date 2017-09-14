while True:
    n=float(input())
    if n==0.00:
        break
    i=2
    sum=0
    while sum<n:
        sum=sum+(1/i)
        i+=1
    print(str(i-2)+" card(s)")
