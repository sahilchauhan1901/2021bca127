x=list(map(int,input('enter the no:').split(" ")))
sum_even=0
sum_odd=0
for i in x:
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print(f"Sum of even no's is:{sum_even}")
print(f"Sum of odd no's is:{sum_odd}")
