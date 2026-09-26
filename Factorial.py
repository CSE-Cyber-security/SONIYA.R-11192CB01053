print("Factorial ")
while(True):
    a=int(input("Enter The Number:"))
    fact=1
    for i in range(1,a+1):
        fact=i*fact
    print("Factorial of",a,"is",fact)
