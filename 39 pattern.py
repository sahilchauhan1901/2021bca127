num = int(input('Enter Number : '))

for i in range(1, num + 1):
    c = 1
    for j in range(1, 2 * i):
        print(c, end=' ')
        if j < i:
            c += 1
        else:
            c -= 1
    print()
