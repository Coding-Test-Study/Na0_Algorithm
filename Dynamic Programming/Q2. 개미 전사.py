n = int(input())
wh = list(map(int, input().split()))

dp = [0]*n

dp[0] = wh[0]
dp[1] = max(wh[0],wh[1])

for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2]+wh[i])

print(dp[n-1])


'''
dp[0] = wh[0]
dp[1] = max(wh[0], wh[1])
dp[2] = max(dp[0] + wh[2], dp[1]) = max(dp[i-2] + wh[i], dp[i-1])
.
.
'''