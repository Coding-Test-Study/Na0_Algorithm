n, m = map(int, input().split())
a, b, d = map(int, input().split())

space = [] # 지도 저장할 리스트
move = [[-1,0],[0,-1],[1,0],[0,1]] # d=0,1,2,3(북, 동, 남, 서)일 때 앞으로 이동하는 값
visit = 1 # 방문한 칸의 수 

# 지도를 2차원 리스트로 저장 [[1,2,3,4],[1,2,3,4],,]
for i in range (n):
    line = list(map(int,input().split()))
    space.append(line)

dx, dy = 0, 0 # 이동하는 값
count = 0 # 주위가 다 바다거나 이미 들렸던 곳 일때

while True:
    d = (d+1)%4 # 방향 바꾸기 (0~3)
    dx, dy = move[d] # 방향에 맞게 이동해야 하는 값
    if 0<=a+dx<n and 0<=b+dy<m: #이동할 위치가 map안에 존재할 때만
        if space[a+dx][b+dy]==1: # 가본 곳이거나 바다
            count += 1
            if count == 4: # 주위가 다 가본 곳이거나 바다
                count = 0
                if(space[a-dx][b-dy]==1): # 바라보는 방향 유지한 채 back한 곳도 바다
                    break
                else: # back
                    a -= dx
                    b -= dy
                    continue
        else: # 육지
            space[a][b] = 1 # 들린 곳임을 표시
            a += dx
            b += dy
            visit += 1
            count = 0

print(visit)

"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""