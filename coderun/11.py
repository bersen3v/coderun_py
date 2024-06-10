# n = int(input())
# graph : dict[int, list]= {}
# for i in range(n):
#     stroka = list(map(int, input().split()))
#     graph[i] = [i for i in range(n) if stroka[i] == 1]

# def dfs(start: int, road: int = -1, seen: list = []):
#     seen.append(start)
#     global graph
    
#     sosedi :list = graph[start] 
#     for sosed in sosedi:
#         if sosed!=road:
#             if sosed in seen:
#                 return True, [i+1 for i in seen]
#             dfs(start=sosed, road=start, seen=seen)
#     return [False]

# for node in graph:
#     answer = dfs(start = node, seen = [])
#     if answer[0] == True:
#         print('YES')
#         print(len(answer[1]))
#         print(*answer[1], sep=" ")
#         print()
# else:
#     print("NO")

n,m = list(map(int, input().split()))
g = [[] for _ in range(n)]

for i in range(m):
    row = list(map(int, input().split()))
    g[row[0]-1].append(row[1]-1)
    g[row[1]-1].append(row[0]-1)
 
def dfs(v, g, used, p):
    used[v] = 1
    for i in g[v]:
        if used[i] == 0:
            p[i] = v
            res = dfs(i, g, used, p)
            if res != None:
                return res
        elif used[i] == 1 and i != p[v]:
            return v, i
 
used = [0] * n
p = [-1] * n
 
for i in range(n):
    if used[i] == 0:
        val = dfs(i, g, used, p)
        if val != None:
            v, i = val
            cycle = [v]
            while v != i:
                v = p[v]
                cycle.append(v)
            cycle = [i+1 for i in cycle]
            print('NO')
            break
 
if 'cycle' not in locals():
    print('YES')