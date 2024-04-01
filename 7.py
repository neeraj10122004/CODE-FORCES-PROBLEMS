n,m=map(int,input().split(" "))
matrix=[]
for i in range(0,n):
    matrix.append([])
    for j in range(0,m):
        matrix[i].append(".")
cou=0
for kk in range(0,n):
    if(kk%2==0):
        if(cou==0):
            poi=-1
            cou=1
        else:
            poi=0
            cou=0
        for i in range(0,m):
            matrix[kk][i]='#'
        for j in range(kk,kk+2):
            if(j<n):
                matrix[j][poi]='#'
aaaa=0
bbbb=0
for i in range(0,n):
    for j in range(0,m):
        print(matrix[i][j],end="")
    print()