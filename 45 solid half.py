num = int(input('Enter Number : '))

for i in range(1, 2*num):
    if i <= num:
        print('* ' * i, end='')
    else:
        print('* ' * (num-i+num), end='')
        
    print()

