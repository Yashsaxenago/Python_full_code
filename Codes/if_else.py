a= int(input("enter your age :"))

print("your age is :", a)

if(a>20):
    print("you are a boy")

else:
    print("you are a men")

#else if 

num=int(input("enter the num :"))

if(num>0):
    print("number is greater than 0")
elif(num==0):
    print("number is to equal to 0")
else:
    print("number is greater than 0")

#nested if else 

sum=int(input("entre the value of sum :"))
print("your sum value is :", sum)

if(sum<0):
    print("sum value is greater than 0")
elif(sum>20):
    if(sum> 20 and sum<=50):
        print("your sum value is between 20 to 50")
    elif(sum>50 and sum<=100):
        print("your sum value is between 50 to 100")
    else:
        print("your sum value is greater than 100")
    
else:
    print("sum is negative")




