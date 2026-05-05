from collections import defaultdict

N = int(input())
d = defaultdict(list)
for _ in range(N):
    d_n = int(input())
    d[d_n].append(d_n)

print(len(d.keys()))
