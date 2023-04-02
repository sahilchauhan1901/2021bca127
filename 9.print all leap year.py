n=int(input('enter the range in year:'))
for i in range(1,n):
    if((i%4==0 or i%4000==0) and i%100!=0):
        print(i)
    else:
        pass