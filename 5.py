a=list(map(int,input().split(" ")))
r=sum(a)
for i in range(min(a),max(a)+1):
    t=(abs(a[0]-i)+abs(a[1]-i)+abs(a[2]-i))
    if(t<r):
        r=t
print(r)