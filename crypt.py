while True:
    m=int(input())
    if m==0:
        break
    text=input()
    text="x"+text
    output=""
    for i in range(1,m+1):
        c=i
        carry=0
        add=(m-i)*2+1
        
        p=(i-1)*2+1
        while c in range(len(text)):
            output+=text[c]
            
            if carry==1:
                c=c+p
                carry=0
            else:
                c=c+add
                carry=1
    print(output) 
    
