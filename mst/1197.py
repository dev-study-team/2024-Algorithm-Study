v,e = map(int, input().split())

edges = []
for _ in range(e):
    edges.append(list(map(int, input().split())))

root = dict()
for i in range(1, v+1):
    root[i] = i

def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]
    
def union(x,y):
    x = find(x)
    y = find(y)

    root[y] = x

edges = sorted(edges, key=lambda x: x[2])

v = 0
for edge in edges:
    if find(edge[0]) == find(edge[1]):
        continue
    else:
        v += edge[2]
        union(edge[0], edge[1])

print(v)