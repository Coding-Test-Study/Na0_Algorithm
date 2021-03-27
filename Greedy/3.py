n, k = map(int, input().split())
count = 0

while n!=1:
    if(n%k != 0):
        count += n%k
        n -= n%k
    if n == 1:
        break
    n //= k
    count += 1

print(count)