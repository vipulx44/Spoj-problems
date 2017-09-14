while True:
    p=input()
    if p=="0":
        break
    lis=[1]
    for i in range(1,len(p)+1):
        if int(p[i])==0:
            if int(p[i-1]+p[i])!=10 and int(p[i-1]+p[i])!=20:
                print(0)
                break
            else:
                lis.append(lis[i-2])
        elif int(p[i-1]+p[i])<=26 and p[i-1]!='0':
            lis.append(int(lis[i-2])+int(lis[i-1]))
        else:
            lis.append(lis[i-1])
        if i==len(p)-1:
            print(lis.pop())

    
