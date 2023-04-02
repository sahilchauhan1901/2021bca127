num = int(input('Enter Number : '))

for i in range(1, num + 1):
    for j in range(1, num - i + 2):
        if j == 1:
            print(i, end=' ')
        elif i == 1:
            print(j, end=' ')
        elif j == num - i + 1:
            print(num, end='')
        else:
            print(' ', end=' ')
    print()
