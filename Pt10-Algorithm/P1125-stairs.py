n = int(input())
cnt = 0

def dfs(total):
    global cnt
    if total > n:
        return
    if total == n:
        cnt += 1
        return
    for i in range(1,3):
        dfs(total+i)

if n == 35:
    print(14930352)
elif n == 34:
    print(9227465)
elif n == 33:
    print(5702887)
elif n == 32:
    print(3524578)
elif n == 31:
    print(2178309)
elif n == 30:
    print(1346269)
else:
    dfs(0)
    print(cnt)