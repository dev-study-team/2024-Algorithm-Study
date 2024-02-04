import sys

sys.setrecursionlimit(10*9)

n,r = map(int, input().split())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):

    a,b,v = map(int, input().split())

    tree[a].append([b,v])
    tree[b].append([a,v])

branch = 0
def dfs1(idx, v):
    global branch
    visited[idx] = True

    # if len(tree[idx]) == 1:
    for nx, nv in tree[idx]:
        if not visited[nx]:
            branch = max(branch, v)
            dfs1(nx, v+nv)
            

branch_idx = 0
column = 0

def dfs2(idx, v):
    global branch_idx, column
    visited[idx] = True

    check = []
    # if len(tree[idx]) >= 3:
    #     return

    for nx, nv in tree[idx]:
        if not visited[nx]:
            check.append([nx,nv])
            column += nv
        
    if len(check) >= 2:
        branch_idx = idx
        column = v
    else:
        if check:
            dfs2(check[0][0], v+check[0][1])

visited = [False] * (n+1)

dfs2(r,0)

visited = [False] * (n+1)

dfs1(branch_idx, 0)

print(str(column) + ' ' + str(branch))


