from collections import deque

def bfs(graph,start,visited=[]):
    queue=deque([start])
    visited[start]=True
    answer=0
    while queue:
        node=queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i]=visited[node]+1
    # 가장 멀리 떨어진 노드 수 계산
    max_edge=max(visited)
    for i in visited:
        if i ==max_edge:
            answer+=1
    return answer

def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    visited=[False]*(n+1)  
    edge.sort()
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    return bfs(graph,1,visited)
    
    
    

























