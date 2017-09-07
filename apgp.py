while True:
    a,b,c=input().split()
    a,b,c=[int(a),int(b),int(c)]
    if a==b==c==0:
        break
    elif b-a==c-b:
        print("AP {}".format(a+3*(b-a)))
    else:
        print("GP {}".format(int(a*(b/a)**3)))
