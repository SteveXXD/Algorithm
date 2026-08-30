def to_base(n,base):
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = digits[n%base] + res
        n //= base
    return res

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a,n,b = line.split()
    a = int(a)
    b = int(b)
    print(to_base(int(n,a),b))