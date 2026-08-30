N = int(input())

def dfs(cash,path):
    if cash == N:
        print(path)
        return
    for m in range(30):
        if cash + ((-1)**m)*(2**m) > N:
            continue