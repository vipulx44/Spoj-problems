nofc=int(input())
for i in range(nofc):
    blank=input()
    exp=input().split()
    for i,a in enumerate(exp):
        if "machula" in a:
            index=i
    if index==4:
        exp[4]=str(int(exp[0])+int(exp[2]))
    elif index==2:
        exp[2]=str(int(exp[4])-int(exp[0]))
    else:
        exp[0]=str(int(exp[4])-int(exp[2]))
    print("{} + {} = {}".format(exp[0],exp[2],exp[4]))
        
    
