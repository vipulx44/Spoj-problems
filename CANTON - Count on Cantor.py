nofc=int(input())
lis=[0,1]
for i in range(2,4500):
    if i%2==0:
        lis.append(lis[i-1]+1)
    else:
        lis.append(i*(i//2+1))
for i in range(nofc):
    num=1
    den=1
    x=int(input())
    j=0
    while x>=lis[j]:
        j+=1
    j-=1
    diff=x-lis[j]
    if diff<=j-1:
        num=diff+1
        den=j-diff
    else:
        diff=x-(lis[j]+j)
        num=j+1-diff
        den=diff+1
    print("TERM {} IS ".format(x)+str(num)+"/"+str(den))
