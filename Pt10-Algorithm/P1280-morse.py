#注意数字电码差异

m = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '.----', '1': '..---', '2': '...--', '3': '....-', '4': '.....',
    '5': '-....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

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

l = list(input())
res = []
for i in range(len(l)):
    res.append(m[l[i]])
print("===".join(res))

