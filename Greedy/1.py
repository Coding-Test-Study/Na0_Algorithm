# n, m, k를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())
# 더한 값을 저장할 변수
count = 0

# n개의 수를 공백으로 구분하여 리스트에 입력받기
li = []
li = list(map(int, input().split()))

# 가장 큰수
max_1 = max(li)
# 가장 큰 수 리스트에서 제거
li.remove(max_1)
# 그 다음 큰 수 
max_2 = max(li)

while m > 0:
    for i in range(0,k):
        if m==0:
            break
        count += max_1
        m -= 1
    if m==0:
        break
    count += max_2
    m -= 1

print(count)
