nofcases=int(input())
for i in range(nofcases):
    x=int(input())
    mylis=[p for p in range(1,x+1)]
    l=len(mylis)
    odd=l%2
    if odd:
        for i in range(0,l-1,2):
            print(i)
            temp=mylis[i]
            mylis[i]=mylis[i+1]
            mylis[i+1]=temp
        temp=mylis[-1]
        mylis[-1]=mylis[-2]
        mylis[-2]=temp
    else:
        for i in range(0,l,2):
            temp=mylis[i]
            mylis[i]=mylis[i+1]
            mylis[i+1]=temp
    print(mylis)    
