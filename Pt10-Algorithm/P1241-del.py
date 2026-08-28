import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    c = list(line)
    tail = 0
    res = []

    for i in range(len(c)-1, -1, -1):
        if c[i] != "*":
            break
        tail += 1
    for _ in range(tail):
        c.pop()

    for i in range(len(c)):
        if c[i] != "*":
            res.append(c[i])

    res += ["*"] * tail
    print("".join(res))