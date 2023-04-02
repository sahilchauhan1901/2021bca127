n=int(input('enter the no of rows:'))
for i in range(0,n+1):
    for j in range(n-i):
        print('',end=' ')
    for k in range(0,i):
        print('*',end=' ')


    print()
