nofcases=int(input())
for i in range(nofcases):
    input()
    ng,nm=input().split()
    ng,nm=[int(ng),int(nm)]
    g=[int(x) for x in input().split()]
    m=[int(x) for x in input().split()]
    maxg=max(g)
    maxm=max(m)
    if maxg<maxm:
       print("MechaGodzilla")
    else:
       print("Godzilla")

