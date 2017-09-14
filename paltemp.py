numoft=int(input())
for i in range(numoft):
    a=input()
    a1=list(str(int(a)+1))
    l=len(a1)
    for j in range(0,l//2):
        a1[l-1-j]=a1[j]
    if int("".join(a1))>int(a):
         print(int("".join(a1)))
    else:
        mid=(l-1)//2
        if a1[mid]=="9":
            while a1[mid]=="9":
                a1[mid]="0"
                a1[l-1-mid]="0"
                mid-=1
            a1[mid]=str(int(a1[mid])+1)
            a1[l-1-mid]=a1[mid]
            print(int("".join(a1)))
        else:
            a1[mid]=str(int(a1[mid])+1)
            a1[l-1-mid]=a1[mid]
            print(int("".join(a1)))
                
        
    
