num = int(input('Enter Number : '))

for i in range(num):
    for j in range(1, num - i + 1):
        print(j, end=' ')
    print()
