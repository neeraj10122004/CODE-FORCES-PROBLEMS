a=[]
for i in range(0,5):
    a.append(list(map(int,input().split(" "))))

x=0
for i in a:
    if 1 in i:
        break
    x+=1
y=0
for y in range(0,5):
    if a[x][y]==1:
        break

print(abs(2-x)+abs(2-y))