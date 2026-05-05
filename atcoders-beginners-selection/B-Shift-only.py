def solve():
    # 入力
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    
    while True:
        if any(x % 2 != 0 for x in a):
            break
        a = [x // 2 for x in a]
        count += 1
    
    print(count)

if __name__ == "__main__":
    solve()
