def dp(n,dic):
    if n in dic:
        return dic[n]
    if n==0:
        return 0
    else:
        m=max(n,dp(int(n/2),dic)+dp(int(n/3),dic)+dp(int(n/4),dic))
        if m not in dic:
            dic[n]=m
        return m
try:
    while True:
        n=input()
        dic={}
        print(dp(int(n),dic))
except:
    pass
