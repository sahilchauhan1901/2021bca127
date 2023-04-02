num = int(input('Enter Number : '))

for i in range(num):
    print(' ' * (num-i-1), end='')
    for j in range(1, i + 2):
        print('*', end=' ')
    print()
for i in range(num):
    print(' ' * (i), end='')
    for j in range(num - i, 0, -1):
        print('*', end=' ')
    print()
