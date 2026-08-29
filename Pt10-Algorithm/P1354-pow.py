import sys,re

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    m = re.match(r"pow\((\d+),(\d+)\)", line)
    a = int(m.group(1))
    b = int(m.group(2))
    print(pow(a%10,b,10))