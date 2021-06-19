"""
위상 정렬은 DAG(Direct Acyclic Graph)에 대해서만 수행 가능
여러 가지 답이 존재할 수 있음
모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단 가능
"""

from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 달기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

print(graph)