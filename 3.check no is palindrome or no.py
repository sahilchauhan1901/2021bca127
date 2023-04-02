n=int(input('enter the no:'))
rem=0
n1=n
p=0
while(n!=0):
    rem=n%10
    p=p*10+rem
    n=n//10
if(p==n1):
    print(f'{n1} no is palindrome')
else:
    print(f'{n1} no is not palindrome')
