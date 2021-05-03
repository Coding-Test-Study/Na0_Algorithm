N = int(input())
component = list(map(int, input().split()))
M = int(input())
order = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid]>target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"

for i in order:
    print(binary_search(component,i,0,N-1),end=" ")