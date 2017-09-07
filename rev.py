def Reverse(a):
    res=0
    while a>0:
        d=a%10
        res=res*10+d
        a=a//10
    return res


n=int(input())
while n>0:
    a,b=input().split()
    a,b=[int(a),int(b)]
    print(Reverse(Reverse(a)+Reverse(b)))
    n-=1


