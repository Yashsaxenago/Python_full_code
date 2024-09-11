
num= int(input("enter the value of num :"))

match num:
    case 0:
        print("num value is zero")
    case 1:
        print("num is not a number")
    case _ if num!=75:
        print(num,"value is not 75")
    
    case _ if num !=85:
        print(num,"value is greater than 75")
    
    case _ :
        print("oops you are wrong way")
