import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단 경로는 0
    heapq.heappush(q,(0,start)) # q = [(0,start)]
    distance[start] = 0

    # 큐가 비어있지 않을 때
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]  # i[1]은 비용
            print(now, cost)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
