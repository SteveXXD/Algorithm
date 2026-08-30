def edit_distance(s,t):
    m,n = len(s),len(t)
    prev = list(range(n+1))
    for i in range(1,m+1):
        cur = [i] + [0] * n
        for j in range(1,n+1):
            cost = 0 if s[i-1] == t[j-1] else 1
            cur[j] = min(prev[j] +1,cur[j-1]+1,prev[j-1] + cost)
        prev = cur
    return prev[n]

print(edit_distance("horse","ros"))