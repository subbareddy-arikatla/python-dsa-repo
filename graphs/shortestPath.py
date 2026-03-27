def bfs(graph,s,par,dist):
    q=deque()
    dist[s]=0
    q.append(s)
    while q:
        node=q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor]==float('inf'):
                par[neighbor]=node
                dist[neighbor]=dist[node]+1
                q.append(neighbor)
                


def print_shortest_distance(graph, S, D, V):
    par=[-1]*V
    dist=[float('inf')]*V
    bfs(graph,s,par,dist)
    if dist[D]==float('inf'):
        print("source and desitination are connect")
        return

if __name__=='__main__':
    v=8
    s,d=2,6
    edges = [
        [0, 1], [1, 2], [0, 3], [3, 4],
        [4, 7], [3, 7], [6, 7], [4, 5],
        [4, 6], [5, 6]
    ]
    graph=[[] for _ in range(v)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        print_shortest_distance(graph,s,d,v)