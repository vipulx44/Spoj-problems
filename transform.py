n=int(input())
for i in range(n):
    stack=[]
    output=""
    text=input()
    for c in text:
        if c is '(':
            stack.append(c)
        elif c in '+-*/^':
            stack.append(c)
        elif c in 'abcdefghijklmnopqrstuvwxyz':
            output+=c
        elif c is ")":
            output+=stack.pop()
            stack.pop()
    print(output)
