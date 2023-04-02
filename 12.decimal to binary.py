num=int(input('enter the no:'))
n=num
bin=0
c=0
while(n>0):
    r=n%2
    bin= r * 10**c +bin
    n=n//2
    c+=1
print(f"{num} in decimal={bin}  binary")