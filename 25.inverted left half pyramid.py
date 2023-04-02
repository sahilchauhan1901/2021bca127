n=int(input('enter the no of rows:'))
for i in range(n,0,-1):
    for k in range(n-i):
        print('',end=' ')
    for j in range(i):
        print('*',end='')
    print()
