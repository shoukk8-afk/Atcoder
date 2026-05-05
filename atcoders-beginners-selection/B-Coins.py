from itertools import product

A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0
for a, b, c in product(range(A + 1), range(B + 1), range(C + 1)):
    if 500 * a + 100 * b + 50 * c == X:
        count += 1
print(count)
