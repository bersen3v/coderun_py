import random

n,m = list(map(int, input().split()))
rebra: dict[int, set] = {}
for _ in range(m):
    x,y = list(map(int, input().split()))
    if x not in rebra:
        rebra[x] = ()
    if y not in rebra:
        rebra[y] = ()
    rebra[x].append(y)
    if x!=y:
        rebra[y].append(x)

# n = random.randint(1,10)
# m = random.randint(0,50)

# answer = []
# seen = []
# def dfs(x:int):
#     global answer
#     if x in seen:
#         return 
    
#     seen.append(x)

#     if x not in answer:
#         answer.append(x)
#         answer = sorted(answer)

#     if x in rebra:
#         for sosed in rebra[x]:
#             dfs(sosed)

# dfs(1)
# print(len(answer))
# newanswer = ''
# for num in answer:
#     newanswer+=str(num)+" "
# if m == 0:
#     print(0)
#     print()
# else:
#     print(newanswer)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

print(dfs(rebra, 1))



    