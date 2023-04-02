num = int(input('Enter Number : '))

for i in range(1, num + 1):
    print(' ' * (num - i), end='')
    for j in range(1, i + 1):
        if i == num or j == 1 or j == i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()
