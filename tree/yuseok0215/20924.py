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



#######

from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**9)

def get_maxbranch(tree, root):
    if root not in tree : return 0

    maxbranch = 0
    for node, w in tree[root].items():
        del tree[node][root]
        branch = w + get_maxbranch(tree, node)
        if branch > maxbranch :
            maxbranch = branch
    return maxbranch

# 변수초기화
N, R = map(int, stdin.readline().split())
tree = defaultdict(dict)
for _ in range(N-1):
    a, b, w = map(int, stdin.readline().split())
    tree[a][b] = w
    tree[b][a] = w

# 기가노드까지의 기둥 길이 찾기
giganode = R
gigalen = 0
while len(tree[giganode])==1:
    node, w = list(tree[giganode].items())[0]
    del tree[node][giganode]
    gigalen += w
    giganode = node

# 가장 긴 가지 길이 찾기
maxbranch = get_maxbranch(tree, giganode)

print('{} {}'.format(gigalen, maxbranch))