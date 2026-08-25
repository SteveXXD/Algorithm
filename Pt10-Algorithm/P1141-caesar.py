import sys

for line in sys.stdin:
    line = line.strip()
    if line == "ENDOFINPUT":
        break
    if line in ("START", "END"):
        continue
    out = []
    for c in line:
        if "A" <= c <= "Z":
            out.append(chr((ord(c)-ord("A")-5)%26 + ord("A")))
        else:
            out.append(c)
    print("".join(out))