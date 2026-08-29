n = int(input())
s = []
find = False
for _ in range(n):
    sn = sorted(input().split())
    if sn in s:
        print("Twin snowflakes found.")
        find = True
        break
    else:s.append(sn)

if not find:
    print("No two snowflakes are alike.")