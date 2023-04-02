x=list(map(int,input('enter the no:').split(" ")))
small=large=x[0]
for i in x:
    if i<small:
        small=i
    if i>large:
        large=i
print(f"The smallest no in the list is: {small}")
print(f"The largest no in thw list is:{large}")