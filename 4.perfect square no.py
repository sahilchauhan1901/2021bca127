n=int(input('enter the no:'))
for i in range(1,n//2):
    if i*i==n:
        print(f'{n} is a perfect square no')
        k=1
        break
if k==0:
    print(f'{n} is not a perfect saure no')
