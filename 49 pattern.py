num = int(input('Enter Number : '))


for i in range(num+1):
    k = 0
    for j in range(2*i + 1):
        if j == 0 or j == 2*i:
            print('*', end=' ')
        else:
            if j <= i:
                k += 1
            else:
                k -= 1
            print(k, end= " ")
    print()

for i in range(num - 1, -1, -1):
    k = 0
    for j in range(2 * i + 1):
        if j == 0 or j == 2*i:
            print('*', end=' ')
        else:
            if j <= i:
                k += 1
            else:
                k -= 1
            print(k, end=" ")
    print()
