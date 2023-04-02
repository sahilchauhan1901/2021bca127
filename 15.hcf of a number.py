n1=int(input("enter the first no:"))
n2=int(input("enter the second no:"))
hcf=0
if n1>n2:
    s=n2
else:
    s=n1

for i in range(1,s+1):
    if (n1%i==0 and n2%i==0):
        hcf=i
print(f'The hcf is:{hcf}')