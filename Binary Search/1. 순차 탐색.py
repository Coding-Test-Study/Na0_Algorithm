# 순차 탐색 : 데이터 정렬 여부와 상관없이 가장 앞 원소부터 확인
# 데이터 개수가 N개일 때, 최대 N번의 비교 연산 필요 -> 최악의 시간 복잡도는 O(N)

def sequential_search(n,target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1  # 몇 번째 데이터인지 출력

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0])  # 원소 개수
target = input_data[1]  # 찾고자하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한칸")
array=input().split()

print(sequential_search(n,target,array))