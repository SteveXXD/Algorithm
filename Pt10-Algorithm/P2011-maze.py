n = int(input())
l = list(input())
ls = []

for _ in range(n-1):
    ls.append(input())

def sub(s):
    sbs = []
    for i in range(1,len(s)+1):#子串长度从1到len
        for j in range(0,len(s)-i+1):#子串起点从0到len-i
            sbs.append(s[j:j+i])
    return sbs

res = []
sbl = sub(l)

for ch in sbl:
    b = "".join(ch)
    cnt = 0
    for i in range(n-1):
        if b in ls[i] or b[::-1] in ls[i]:
            cnt += 1
    if cnt == n-1:
        res.append(b)

mx = 0

for p in res:
    if len(p) > mx:
        mx = len(p)

print(mx)