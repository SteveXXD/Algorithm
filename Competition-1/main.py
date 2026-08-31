n,m = map(int,input().split())
mat = [0]*n

for i in range(n):
    mat[i] = list(input())

#print(mat)
b = []

#print(b)

i = 1

for x in range(n):
    for y in range(m):
        if mat[x][y] == ".":
            i += 1
            continue
        else:
            if x == n-1:
                pass
            else:
                if mat[x+1][y] == "#":
                    b.append((i,i+m))
            if x == 0:
                pass
            else:
                if mat[x-1][y] == "#":
                    b.append((i,i-m))
            if y == m-1:
                pass
            else:
                if mat[x][y+1] == "#":
                    b.append((i,i+1))
            if y == 0:
                pass
            else:
                if mat[x][y-1] == "#":
                    b.append((i,i-1))
        i += 1

#print(b)

N = 0

#计算一下节点数。
for x in range(n):
    for y in range(m):
        if mat[x][y] == "#":
            N += 1

#print("节点数",N)

from collections import deque

M = len(b)

#连通分量忘了。网上查的连通分量。
#https://blog.51cto.com/u_16213440/13154454
def bfs_u(v, visited, graph, component):
    queue = deque()
    queue.append(v)
    visited.add(v)
    component.append(v)

    while queue:
        vertex = queue.popleft()
        for neighbour in graph.graph[vertex]:
            if neighbour in graph.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    component.append(neighbour)


def bfs(graph):
    visited = set()
    components = []

    for vertex in graph.get_all_vertices():
        if vertex not in visited:
            component = []
            bfs_u(vertex, visited, graph, component)
            components.append(component)

    return components


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u1, v1):
        self.graph[u1].append(v1)
        self.graph[v1].append(u1)

    def get_all_vertices(self):
        return self.graph.keys()


g = Graph()
for ch in b:
    u, v = ch
    g.add_edge(u, v)

cp = bfs(g)

ct = 0
for h in cp:
    ct += len(h)

if ct < N:
    print(len(cp)+(N-ct))
else:
    print(len(cp))