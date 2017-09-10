n=int(input())
for i in range(n):
    blank=input()
    noofchild=int(input())
    l=[]
    for i in range(noofchild):
        l.append(int(input()))
    length=len(l)
    for i,x in enumerate(l):
        if x%length!=0:
            l[i]=(x%length)
    if sum(l)%length==0:
        print("YES")
    else:
        print("NO")
            
