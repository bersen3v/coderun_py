def get_vertex(gr,v,chk):
    res=[]
    for a in gr[v]:
        if a not in chk:
            res.append(a)
    return res        
 
def bfs(gr,start):
    que=[start]
    chk=[start]
    tree=[]
    while (len(que)>0):
        v=que.pop()
        z=get_vertex(gr,v,chk)
        for w in z:
            que=[w]+que
            chk.append(w)
            tree.append((v,w))
    return tree
    
def get_path(tree,start,finish):
    s,f=0,0
    for pair in tree:
        if pair[0]==start:
            s=1
        if pair[1]==start:
            s=1
        if pair[0]==finish:
            f=1
        if pair[1]==finish:
            f=1
    if s==0 or f==0:
        return []
    curr=finish
    length=0
    path=[]
    while curr != start:
        for pair in tree:
            if pair[1]==curr:
                path.append(pair)
                length+=1
                curr=pair[0]
                break
    return (path[::-1],length)        
 
def get_graph():
    n=int(input())
    res=[]
    for _ in range(n):
        v=[]
        tmp=tuple(map(int,input().split()))
        for i in range(n):
            if tmp[i] != 0:
                v.append(i)
        res.append(v)        
    return res
 
def show_path(pth):
    print(pth[1])
    if pth[1]!=0:
        for pair in pth[0]:
            print(pair[0]+1,end=' ')
        print(pair[1]+1)    
        
    
def search(graph,start,finish):
    tr=bfs(graph,start)
    return get_path(tr,start,finish)
    
def task():
    graph=get_graph()
    start,finish=map(int,input().split())
    pth=search(graph,start-1,finish-1)
    if len(pth)==0:
        print(-1)
    else:
        show_path(pth)
 
task()