import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    res = []
    n, m = map(int, line.split())
    l = [x for x in range(1, n + 1)]
    i = 0

    while len(l) != 0:
        i = (i + m - 1) % len(l)
        res.append(str(l.pop(i)))
    print(' '.join(res))