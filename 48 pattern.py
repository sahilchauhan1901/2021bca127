num = int(input('Enter Number : '))


k = 1
for i in range(1, num+1):
    for j in range(i):
        print(k, end="")
        if j < i - 1:
            print('*', end='')
        k += 1
    print()

k = int((num * num + num)/2 + 1)
for i in range(num, 0, -1):
    k = k - i
    for j in range(i):
        print(k + j, end='')
        if j < i - 1:
            print('*', end='')
    print()
