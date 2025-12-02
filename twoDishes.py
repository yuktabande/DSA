def solve():
    n, a, b, c = map(int, input().split())
    
    if min(b, a + c) >= n:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()
