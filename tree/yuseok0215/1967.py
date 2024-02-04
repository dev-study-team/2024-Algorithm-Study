n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,v = map(int, input().split())

    tree[a].append((b,v))
    tree[b].append((a,v))

answer = 0

def dfs(start, v):
    global answer
    visited[start] = True

    if len(tree[start]) == 1:
        answer = max(answer, v)
        return start

    for nx, nv in tree[start]:
        if not visited[nx]:
            dfs(nx, v+nv)

visited = [[False] for _ in range(n+1)]
new_start = dfs(1,0)

visited = [[False] for _ in range(n+1)]
dfs(new_start, answer)

print(answer)
