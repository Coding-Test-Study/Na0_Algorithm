# 이진 탐색 : 배열 내부의 데이터가 정렬되어있어야 사용가능.
# 찾으려는 데이터와 중간점 데이터를 반복적으로 비교
# 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어듬. 시간복잡도 O(logN)

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid]==target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target,0,n-1)
if result==None:
    print("존재하지 않습니다.")
else:
    print(result+1)
