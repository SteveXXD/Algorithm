n = int(input())
l = []

for _ in range(n):
    name = input()
    if name != "China":
        l.append(name)

l.sort()
l.append("China")

for ch in l:
    print(ch)