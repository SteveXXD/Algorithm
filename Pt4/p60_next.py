from p54_sqstring import SqString

def next_minus_1(p):
    next = [0] * p.length()
    k = 0
    j = 1
    next[0] = -1
    next[1] = 0
    while j<p.length() -1:
        if p.charAt(j) == p.charAt(k):
            next[j+1] = k + 1
            k += 1
            j += 1
        elif k == 0:
            next[j+1] = 0
            j += 1
        else:
            k = next[k]
    return next

string1 = SqString("abaab")
nxt = next_minus_1(string1)
print(nxt)
