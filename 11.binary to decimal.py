bin=int(input('enter the no in binaary:'))
c=s=0
n=bin
while n>0:
    r=n%10
    s=r* 2**c +s
    n=n//10
    c=c+1
print(f"{bin} number in decimal is {s}")