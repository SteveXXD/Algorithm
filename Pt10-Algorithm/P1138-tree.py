def post(pre, ino):
    if not pre:
        return ""
    root = pre[0]
    k = ino.index(root)
    left_in, right_in = ino[:k], ino[k+1:]
    left_pre, right_pre = pre[1:1+k], pre[1+k:]
    return post(left_pre, left_in) + post(right_pre, right_in) + root

ino = input().strip()
pre = input().strip()
print(post(pre, ino))