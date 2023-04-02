characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = int(input('Enter Number : '))

for i in range(1, num + 1):
    c = 0
    for j in range(0, 2 * i - 1):
        print(characters[c], end=' ')
        if j < i:
            c += 1
        else:
            c -= 1
    print()
