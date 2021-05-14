n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3,n+1):
    # i-2일 때 2가지 경우인 이유는 1x2가 i-1, i에 채워지는 경우가 d[i-1]에 포함되었기 때문
    d[i] = (d[i-1] + 2*d[i-2])%796796

print(d[n])