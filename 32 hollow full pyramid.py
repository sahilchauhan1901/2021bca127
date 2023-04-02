num = int(input('Enter Number : '))

for i in range(1, num+1):
    for j in range(i):
        print(" ", end="")

    if i == 1:
        print('* ' * num, end='')
    else:
        for j in range(1, 2 * (num-i) + 2):
            if j == 1 or j == 2 * (num-i) + 1:
                print("*", end="")
            else:
                print(" ", end="")
    print()
