n = int(input())
seq = [1, 2, 0, 2, 2, 1, 0, 1]
print("yes" if seq[n % 8] == 0 else "no")