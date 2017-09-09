try:
    while True:
        n=int(input())
        dic={}
        for i in range(n+1):
            if i==0:
                dic[i]=0
            elif i==1:
                dic[i]=1
            else:
                dic[i]=max(i,dic[int(i/2)]+dic[int(i/3)]+dic[int(i/4)])
        print(dic[n])
except:
    pass
