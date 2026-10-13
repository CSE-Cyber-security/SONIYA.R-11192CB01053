while(True):
    print("\n \n FIBONACCI SERIES")
    a=0
    b=1
    n=int(input("Enter the number of terms:"))
    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
        
        
