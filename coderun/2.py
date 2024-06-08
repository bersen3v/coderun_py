def createMatrix() -> list[list[int]]:    
    nm : list[int] = list(map(int, input().split()))
    n, m = nm

    matrix : list[list[int]]= []
    for i in range(n):
        new = list(map(int, input().split()))
        matrix.append(new)
    
    return matrix, n, m

res : list[int] = []

def search(matrix : list[list[int]], 
           start : list[int], 
           end : list[int], 
           road : list[int]):
    
    if start == end:
        road.append(matrix[start[0]][start[1]])
        res.append(sum(road))
        return
    
    if start[0] != end[0]:
        search(matrix, [start[0]+1, start[1]], end, road + [matrix[start[0]][start[1]]])
    
    if start[1] != end[1]:
        search(matrix, [start[0], start[1]+1], end, road + [matrix[start[0]][start[1]]])
    
matrix, n, m = createMatrix()
search(matrix, [0,0], [n-1,m-1], [])
print(min(res))