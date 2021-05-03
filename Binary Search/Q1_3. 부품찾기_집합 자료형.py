n = int(input())

# 전체 부품번호 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print("yes",end=" ")