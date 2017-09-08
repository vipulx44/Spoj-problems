n=int(input())
while n>0:
    a,b=input().split()
    a,b=[int(a),int(b)]
    ud=a%10
    b4=b%4
    b3=b%3
    b2=b%2
    if ud==1 or ud==5 or ud ==6 or ud==0:
        print(ud)
    elif ud==2:
        if b4==0:
            print("6")
        elif b3==0:
            print("8")
        elif b2==0:
            print("4")
        else:
            print("2")
    elif ud==3:
        if b4==0:
            print("1")
        elif b3==0:
            print("7")
        elif b2==0:
            print("9")
        else:
            print("3")
    elif ud==4:
        if b2==0:
            print("6")
        else:
            print("4")
    elif ud==7:
        if b4==0:
            print("1")
        elif b3==0:
            print("3")
        elif b2==0:
            print("9")
        else:
            print("7")
    elif ud==8:
        if b4==0:
            print("6")
        elif b3==0:
            print("2")
        elif b2==0:
            print("4")
        else:
            print("8")
    elif ud==9:
        if b2==0:
            print("1")
        else:
            print("9")
    n-=1
