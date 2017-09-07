n=int(input())
for i in range(n):
    a,b=input().split()
    a,b=[int(a),int(b)]
    if a==b:
        if a%2==0:
            print(a*2)
        else:
            print(a*2-1)
    elif a-b==2:
        if a%2==0:
            print(a+b)
        else:
            print(a+(b-1))
    else:
        print("No Number")
            
    
