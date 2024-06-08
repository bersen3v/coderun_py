def createMatrix() -> list[list[int]]:    
    nm : list[int] = list(map(int, input().split()))
    n, m = nm

    matrix : list[list[int]]= []
    for i in range(n):
        new = list(map(int, input().split()))
        matrix.append(new)
    
    return matrix, n, m

matrix, n, m = createMatrix()
def dynamicSearch():
    global matrix, n, m
    for y in range(n):
        for x in range(m):
            up = None
            left = None
            if y!=0: 
                up = matrix[y-1][x]
            if x!=0: 
                left = matrix[y][x-1]
            if None not in [up, left]:
                matrix[y][x] = min(left, up) + matrix[y][x]
            elif left == None and up!=None:
                matrix[y][x] += up
            elif left!=None and up==None:
                matrix[y][x] += left

dynamicSearch()
print(matrix[n-1][m-1])