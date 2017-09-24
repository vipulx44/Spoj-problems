while True:
    n=int(input())
    if n==0:
        break
    inq=[int(x) for x in input().split()]
    s=[]
    oq=[]
    for i in range(len(inq)):
        if i==0:
            s.append(inq[i])
        elif inq[i]<s[len(s)-1]:
            s.append(inq[i])
        else:
            while s and inq[i]>s[len(s)-1]:
                oq.append(s.pop())
            s.append(inq[i])
    for i in range(len(s)):
        oq.append(s.pop())
    ans=all(oq[i-1]<oq[i] for i in range(1,len(oq)))
    if ans:
        print("yes")
    else:
        print("no")
    
