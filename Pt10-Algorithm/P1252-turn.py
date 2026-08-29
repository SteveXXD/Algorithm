import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    matrix = [[0] * n for _ in range(n)]

    for x in range(n):
        k = n - x - 1
        for y in range(x + 1):
            matrix[x][y] = n - x
        for y in range(x + 1, n):
            matrix[x][y] = k
            k -= 1

    for i in range(n):
        print(" ".join((map(str, matrix[i]))))

