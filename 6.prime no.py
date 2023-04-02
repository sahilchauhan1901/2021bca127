n=int(input('enter the no:'))
k=0
if (n == 2):
    print('prime no')
for i in range(2,n):
    if(n%i==0):
        k=k+1
        break
    else:
        pass
if(k!=1):
    print(f'{n} is a prime no')
else:
    print(f"{n} is not a prime no")

