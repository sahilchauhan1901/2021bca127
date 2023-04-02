num = int(input('Enter Number : '))

for i in range(num):
    print(' ' * (num-i-1), end='')
    for j in range(1, i + 2):
        if j == 1 or j == i+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(num):
    print(' ' * (i), end='')
    for j in range(num - i, 0, -1):
        if j == num-i or j == 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
