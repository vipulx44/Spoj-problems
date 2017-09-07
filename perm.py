m=input()
l=[]
o=""
def perm(o):
    for i in m:
        if i in l:
            continue
        l.append(i)
        o+=i
        if len(o)==len(m):
              print(o)
        perm(o)
        o=o[0:len(o)-1]
        l.remove(i)

perm(o)
