num = int(input('Enter Number : '))


for i in range(1, num+1):
    for j in range(i):
        print(i,end="")
        if j < i - 1:
            print('*',end='')   
    print()

for i in range(num, 0, -1):
    for j in range(i):
        print(i,end='')
        if j < i - 1:
            print('*', end='')
    print()


