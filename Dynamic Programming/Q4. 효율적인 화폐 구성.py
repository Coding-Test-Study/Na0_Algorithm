n, m = map(int, input().split())
v = []

for i in range(n):
    v.append(int(input()))


d = [10001]*(m+1)
d[0] = 0

for i in range(n): # 모든 화폐 가치에 대해
    for j in range(v[i],m+1):
        if d[j-v[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j],d[j-v[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])