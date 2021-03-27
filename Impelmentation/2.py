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