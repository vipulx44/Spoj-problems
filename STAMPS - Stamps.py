nofcase=int(input())
for i in range(nofcase):
    tm,b=input().split()
    tm,b=[int(tm),int(b)]
    m=[int(x) for x in input().split()]
    s=0
    count=0
    if sum(m)>=tm:
        while s<tm:
            s+=max(m)
            m.remove(max(m))
            count+=1
        print("Scenario #{}:".format(i+1))
        print(count)
    else:
        print("Scenario #{}:".format(i+1))
        print("impossible")
    print()
