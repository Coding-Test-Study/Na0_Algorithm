n = int(input())
count = 0

for i in range(0,n+1):
    # 시에 3이 들어갈 때
    if i%10==3 or 30<=i<=39:
        count += 60*60
    else:
        for j in range(0,60):
            # 분에 3이 들어갈 때
            if j%10==3 or 30<=j<=39:
                count += 60
            else:
                for k in range(0,60):
                    # 초에 3이 들어갈 때
                    if k%10 == 3 or 30<=k<=39:
                        count += 1

print(count)

"""
n = int(input())
ans = 0

for a in range(n+1):
    if "3" in str(a):
        ans += 60*60
        continue
        
    for b in range(60):
        if "3" in str(b):
            ans += 60
            continue
        for c in range(60):
            if "3" in str(c):
                ans += 1

print(ans)
"""
