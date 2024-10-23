for i in range(12):
    if(i==12):
        break
    print("5 X", i+1, "=" ,5*(i+1))

print("out of the loop")


for i in range(25):
    if(i==10 or i==21):
        continue
 
    print("the value of i is ", i)