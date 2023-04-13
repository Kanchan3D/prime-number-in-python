n=int(input("neter"))
p=0
i=2
while(i<=n):
    if(n%i==0):
        p=p+1
    i=i+1
    print("the entered number is a prime number")
else:
    print("the entered number is not a prime number")
print(i)