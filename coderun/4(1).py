n,m = list(map(int, input().split()))

matrix = []
submatrix = []
for y in range(n):
    submatrix = [0 for _ in range(m)]
    for x in range(m):
        if x==0 and y==0:
            submatrix[x]+=1
        if y>=2 and x>=1:
            submatrix[x]+=matrix[y-2][x-1]
        if y>=1 and x>=2:
            submatrix[x]+=matrix[y-1][x-2]           
    matrix.append(submatrix)
print(submatrix[-1])
        