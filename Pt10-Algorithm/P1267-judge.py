
import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a, b, c = map(int, line.split())
    if a+b<=c or a+c <=b or b+c <=a:
        print("not a triangle")
        continue
    if a == b == c:
        print("regular triangle")
        continue
    if a == b or b == c or c == a:
        print("isosceles triangle")
        continue
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        print("right triangle")
        continue
    print("triangle")