from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(0,n):
    graph.append(list(map(int,input())))

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(x,y): 
    queue = deque()
    queue.append((x,y))

    #큐가 빌 때 까지
    while queue:
        x, y = queue.popleft()

        for i in range(0,4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1: #괴물이 없으면
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))

"""
5 6
101010
111111
000001
111111
111111
"""