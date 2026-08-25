from collections import deque

T = int(input())
for _ in range(T):
    k = int(input())
    s = input().strip()
    if s[0] == '*' or s[-1] == '*':
        print("NO")
        continue
    ats = [i for i, c in enumerate(s) if c == '@']
    vis = [False] * k
    q = deque([0])
    vis[0] = True
    ok = False
    while q:
        x = q.popleft()
        if x == k - 1:
            ok = True
            break
        for nx in (x - 1, x + 1):
            if 0 <= nx < k and not vis[nx] and s[nx] != '*':
                vis[nx] = True
                q.append(nx)
        if s[x] == '@':
            for nx in ats:
                if not vis[nx]:
                    vis[nx] = True
                    q.append(nx)
    print("YES" if ok else "NO")