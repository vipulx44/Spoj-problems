import random
a=int(input("Enter Lower Bound: "))
b=int(input("Enter Higher Bound: "))
val=int(input("Enter your Value:"))
print("Your Value is %s" % val)
while True:
    guess=int((b+a)/2)
    inp=input("Is the value %s? :  " % {guess})
    if inp=='Yes' and val==guess:
        print("I am the best")
        break
    elif inp=="higher":
        a=guess
    elif inp=="lower":
        b=guess
