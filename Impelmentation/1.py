n = int(input())
plan = list(input().split())

x = 1
y = 1
mx = [0,0,-1,1]
my = [1,-1,0,0]
direction = ['R','L','U','D']

for i in plan:
    n_x = x + mx[direction.index(i)]
    n_y = y + my[direction.index(i)]

    if n_x < 1 or n_x > n or n_y < 1 or n_y > n:
        continue
    else:
        x = n_x
        y = n_y

print(x, y)

"""
n = int(input())
m = list(input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
d = {'L':(0,-1), 'R':(0,1), 'U':(-1, 0), 'D':(1, 0)}

x, y = 1, 1

for a in m:
    nx, ny = x + d[a][0], y + d[a][1]
    
    if 1<=nx<=n and 1<=ny<=n:
        x, y = nx, ny

print(x, y)
"""
