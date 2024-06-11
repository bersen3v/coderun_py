n, m, s, t, q = list(map(int, input().split()))
n+=1
m+=1

matrix = [[0 for _ in range(m)] for _ in range(n)]
print(s,t)
matrix[s][t] = 2

def bfs(start: tuple[int, int], road: list, end: tuple[int, int] = (s,t)):
    print(start, end)
    if start==end:
        return True
    
    xPos = [-2,2,-2,2,-1,-1,1,1]
    yPos = [1,1,-1,-1,2,-2,2,-2]

    for i in range(len(xPos)):
        if 0<=xPos[i]<=m and 0<=yPos[i]<=n:
            return bfs(start=(yPos[i], xPos[i]), road=road + [start])

for blohaPlace in range(q):
    y,x = list(map(int, input().split()))
    print(bfs(start=(y,x), road=[]))
    matrix[y][x] = 1

print(matrix)






