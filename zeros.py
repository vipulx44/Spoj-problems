n=int(input())
for i in range(n):
    m=int(input())
    sr=5
    zeros=0
    while sr<=m:
        zeros=zeros+int(m//sr)
        sr=sr*5
    print(zeros)
