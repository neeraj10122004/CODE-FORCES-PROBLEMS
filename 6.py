nn=int(input())
ret=[]
for j in range(0,nn):
    a=list(input())
    a=a[::-1]
    a=list(map(int,a))
    for i in range(0,len(a)):
        a[i]=a[i]*(10**i)
    while(0 in a):
        a.remove(0)
    ret.append(a)
    
for j in range(0,nn):
    print(len(ret[j]))
    for i in ret[j]:
        print(i,end=" ")
    print()
    