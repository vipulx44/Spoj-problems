n=int(input())
while n>0:
    a,b=input().split()
    a,b=[int(a),int(b)]
    ud=a%10
    b4=b%4
    if b==0:
        print("1")
    elif ud==1 or ud==5 or ud==6 or ud==0:
        print(ud)
    elif b==0:
        print("1")
    else:
        if b4==0:
            p=ud**4
            print(p%10)
        elif b4==1:
            p=ud**1
            print(p%10)
        elif b4==2:
            p=ud**2
            print(p%10)
        else:
            p=ud**3
            print(p%10)
    n-=1
