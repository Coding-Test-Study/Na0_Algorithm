# 다시 풀어보기

n, m = map(int,input().split())
frame = [[0]*m]*n
ic = True

for i in range(0,n):
    frame[i] = list(map(int, input()))

def ice(a,b):
    if a<0 or a>=n or b<0 or b>=m: # 프레임 밖
        return False
    if frame[a][b]==0:
        frame[a][b] = -1
        ice(a-1,b) #상
        ice(a+1,b) #하
        ice(a,b-1) #좌
        ice(a,b+1) #우
        return True
    else:
        return False
    
count = 0
for a in range(0,n):
    for b in range(0,m):
        # 한 점에 대해 dfs를 수행하면 연결돼있는 0 값을 모두 방문할 수 있음.
        # 갈 수 있는 모든 곳을 방문한 후에는 True 리턴
        if ice(a,b) == True: 
            count +=1

print(count)

"""
4 5
00110
00011
11111
00000
"""