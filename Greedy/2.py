n, m = map(int, input().split()) 

li = []
min_card = [];

for i in range(0,n):
    li += list(map(int, input().split()))

for i in range(0,m):
    # 각 행의 첫 번째 값을 temp에 저장
    temp = li[i]

    # 각 행의 최소 값을 새로운 리스트 min_card에 저장
    for j in range(0,n):
        print(i*n + j)
        if li[i*n + j] < temp:
            temp = li[i*(n-1)+ j]
    min_card.append(temp)

print(min_card)
