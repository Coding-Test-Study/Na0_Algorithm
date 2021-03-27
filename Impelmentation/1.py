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