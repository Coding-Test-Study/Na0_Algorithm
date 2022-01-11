n = input()

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

count = 0

for i in range(8):
    if ord('a')<=ord(n[0])+dx[i]<=ord('h'):
            if 1<=int(n[1])+dy[i]<=8:
                count += 1

print(count)

"""
n = input()
x, y = ord('a') -ord(n[0]) + 1, int(n[1])
cnt = 0

d = [(-2, 1), (-2, -1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2),(1, -2)]

for i in range(8):
    nx, ny = x + d[i][0], y + d[i][1]
    
    if 1<=nx<=8 and 1<=ny<=8:
        cnt+=1
        
print(cnt)
"""
