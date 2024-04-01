a=list(map(int,list(input())))
for i in range(0,len(a)):
    if(4<a[i]):
        a[i]=9-a[i] 
ret=0
i=0
if(a[0]==0):
    a[0]=9
a[::-1]
for j in a:
    ret=(ret*10)+j
print(ret)
    

