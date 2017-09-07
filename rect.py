m=int(input())
total=m
for i in range(2,int((m+1)/2+1)):
    curr=int(m/i)
    if curr>i:
        curr=i
    total+=curr-1
print(total)
