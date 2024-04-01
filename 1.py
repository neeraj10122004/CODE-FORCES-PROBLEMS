x=0
for i in range(int(input())):
    a=input()
    if(a=="++X" or a=="X++"):
        x+=1
    elif(a=="--X" or a=="X--"):
        x-=1
print(x)
