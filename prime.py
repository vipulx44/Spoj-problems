from math import sqrt
        
primes=[2]
for i in range(3,32000,2):
    isprime=True
    sq=sqrt(i)+1
    for j in primes:
        if j>=sq:
            break
        elif i%j==0:
            isprime=False
    if isprime:
        primes.append(i)
    
n=int(input().strip())
output=''
for i in range(n):
    if i > 0:
        output="\n"
    a,b=input().strip().split()
    a,b=[int(a),int(b)]
    sq=sqrt(b)+1
    if a<2:
        a=2

    isprime = [True]*100001

    for i in primes:
        if (i>=sq):
            break

        if i>=a:
            start=i*2
        else:
            start=a+((i-a%i)%i)
        for j in range(start,b+1,i):
            isprime[j-a]=False
    for i in range(a,b+1):
        if isprime[i-a]:
            output += str(i) + "\n"
    print(output[:-1])
