def solve(n):
    if n == 4:
        print("4,5-->9,10")
        print("8,9-->4,5")
        print("2,3-->8,9")
        print("7,8-->2,3")
        print("1,2-->7,8")
    else:
        print(f"{n},{n+1}-->{2*n+1},{2*n+2}")
        print(f"{2*n-1},{2*n}-->{n},{n+1}")
        solve(n-2)
        print(f"{2*n-3},{2*n-2}-->{2*n-1},{2*n}")


import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    solve(n)