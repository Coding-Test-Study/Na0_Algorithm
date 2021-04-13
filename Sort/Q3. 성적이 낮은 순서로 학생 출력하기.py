n = int(input())
array = []

for i in range(n):
    array.append(tuple(input().split()))

def setting(data):
    return int(data[1])
    
array.sort(key=setting)

for i in array:
    print(i[0], end=' ')