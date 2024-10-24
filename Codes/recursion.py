#factorial

def Fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*Fact(n-1)
    
print(Fact(5))

# fibonacci

def Fibo(n):
    if(n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return (Fibo(n-1)+Fibo(n-2))
        
print(Fibo(1))