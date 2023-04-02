num = int(input('Enter Number : '))

for i in range(num):
    print(' ' * i + '* ' * (num - i))
for i in range(2, num + 1):
    print(' ' * (num-i) + '* ' * i)
