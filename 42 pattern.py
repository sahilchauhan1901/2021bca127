num = int(input('Enter Number : '))

for i in range(1, num + 1):
    print('*' * (num - i + 4), end='')
    for j in range(1, i + 1):
        print(i, end='*')
        
    print('*' * (num - i + 3), end='')
    print()
