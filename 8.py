a={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
ret=0
for i in range(int(input())):
    ret+=a[input()]
print(ret+10)