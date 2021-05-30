import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

max_time = 0
count = 0

for i in distance:
    if i != INF and i!=0:
        count += 1
        max_time = max(max_time, i)

print(count, max_time)

"""
3 2 1
1 2 4
1 3 2
"""
