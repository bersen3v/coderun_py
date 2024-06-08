def createMatrix() -> list[list[int]]:    
    nm : list[int] = list(map(int, input().split()))
    n, m = nm

    matrix : list[list]= []
    for i in range(n):
        new = list(map(int, input().split()))
        matrix.append([[i,0,0] for i in new])
    
    return matrix, n, m

matrix, n, m = createMatrix()
def dynamicSearch():
    global matrix, n, m
    for y in range(n):
        for x in range(m):
            up = None
            left = None
            if y!=0: 
                up = matrix[y-1][x][0]
            if x!=0: 
                left = matrix[y][x-1][0]
            if None not in [up, left]:
                if left>up:
                    matrix[y][x] = [left + matrix[y][x][0], [y, x-1],'R ']
                else:
                    matrix[y][x] = [up + matrix[y][x][0], [y-1, x],'D ']
            elif left == None and up!=None:
                matrix[y][x] = [up + matrix[y][x][0], [y-1, x],'D ']
            elif left!=None and up==None:
                matrix[y][x] = [left + matrix[y][x][0], [y, x-1],'R ']

answer = ''
def searchRoad(yx : list[int]):
    global answer
    element = matrix[yx[0]][yx[1]]
    if element[-1] == 0:
        return
    answer += element[-1]
    searchRoad(element[1])
    
    
dynamicSearch()
searchRoad([n-1,m-1])
print(matrix[n-1][m-1][0])
print(answer[::-1][1:])

