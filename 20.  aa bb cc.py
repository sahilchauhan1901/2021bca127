n=int(input('Enter the lines:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),sep=' ',end=' ')
    print()