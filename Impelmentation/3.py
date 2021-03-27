n = input()
dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

count = 0

for i in range(8):
    if ord('a')<=ord(n[0])+dx[i]<=ord('h'):
            if 1<=int(n[1])+dy[i]<=8:
                count += 1
    
print(count)