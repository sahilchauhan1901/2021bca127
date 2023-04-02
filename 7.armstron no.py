n=int(input('enter the no:'))
sum=0
digit=0
cpy=n
order=len(str(n))
while(n!=0):
    digit=n%10
    sum+=digit**order
    n=n//10
if(sum==cpy):
    print('Armstrong no')
else:
    print('not a armstrong no')