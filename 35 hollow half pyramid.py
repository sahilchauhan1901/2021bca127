num = int(input('Enter Number : '))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == num:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()

