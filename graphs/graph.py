n=4
matrix=[[0]*n for _ in range(n)]
edges=[(0,1),(0,2),(1,3),(2,3)]
for u,v in edges:
    matrix[u][v]=1
    matrix[v][u]=1
for row in matrix:
    print(row)
print('directed graph')
n=4
matrix=[[0]*n for _ in range(n)]
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
for u,v in edges:
    matrix[u][v]=1
for row in matrix:
    print(row)

n=4
adj=[[] for _ in range(n)]
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]

for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
for i in range(n):
    print(i,'->',adj[i])

n=4
adj=[[] for _ in range(n)]
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]

for u,v in edges:
    adj[u].append(v)

for i in range(n):
    print(i, "->", adj[i])

n=4 
adj = [
    [1, 2],   # 0
    [3],      # 1
    [3],      # 2
    []        # 3
]
transpose=[[] for _ in range(n)]
for u in range(n):
    for v in adj[u]:
        transpose[v].append(u)

for i in range(n):
    print(i, "->", transpose[i])

graph = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
n=len(graph)
transpose=[[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        transpose[j][i]=graph[i][j]
for row in transpose:
    print(row)

def dfs(node,adj,visited):
    visited[node]=True
    print(node,end=' ')
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor,adj,visited)
adj=[[1],[],[3],[]]
n=len(adj)
visited=[False]*n
for i in range(n):
    if not visited[i]:
        dfs(i,adj,visited)

from collections import deque

def bfs(start,adj,visted):
    q=deque([start])
    visted[start]=True

    while q:
        node=q.popleft()
        print(node,end=' ')
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor]=True
                q.append(neighbor)


adj = [
    [1],
    [],
    [3],
    []
]
n=len(adj)
visited=[False] * n
for i in range(n):
    if not visited[i]:
        bfs(i,adj,visited)
def bfss(start,adj,visted):
    k=deque([start])
    visted[start]=True
    while q:
        node=q.popleft()
        print(node)


adj = [
    [1],
    [],
    [3],
    []
]
n=len(adj)
visited=[False]*n
for i in range(n):
    if not visited[i]:
        bfs(i,adj,visited)