import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    l = list(map(int,line.split("+")))
    print(sum(l))