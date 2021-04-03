n, m = map(int,input().split())
frame = [[0]*m]*n

for i in range(0,n):
    frame[i] = list(map(int,input()))

print(frame)


"""
4 5
00110
00011
11111
00000
"""