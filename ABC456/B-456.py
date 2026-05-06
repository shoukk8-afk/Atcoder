from itertools import product

a = list(input().split())
b = list(input().split())
c = list(input().split())
    
p = product(a, b, c)
total = 0
for comb in p:
    if set(comb) == set(('4', '5', '6')):
        total += 1
print(total / (6 * 6 * 6))
