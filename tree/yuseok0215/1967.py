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


# 다른 풀이

import sys
sys.setrecursionlimit(10**9)  # dfs 반복횟수 제한 해제
input = sys.stdin.readline

# 입력
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append([child, weight])
    graph[child].append([parent, weight])

# dfs
def dfs(x, dist):
    for i in graph[x]:
        node, wei = i
        if distance[node] == -1:
            distance[node] = dist + wei
            dfs(node, dist + wei)

# 1번 노드에서 가장 먼 곳을 찾음
distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

# 찾은 노드에서 가장 먼 노드를 찾음
res = distance.index(max(distance))
distance = [-1] * (n+1)
distance[res] = 0
dfs(res, 0)

# 출력
print(max(distance))