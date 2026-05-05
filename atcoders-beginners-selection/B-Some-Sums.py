N, A, B = map(int, input().split())
total = 0
for n in range(1, N + 1):
    a = n
    sum = 0
    l = map(int, ','.join(str(n)).split(','))
    for i in l:
        sum += i
    if A <= sum <= B:
        total += a
        
print(total)
