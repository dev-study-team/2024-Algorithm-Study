from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)
    
parent = [0] * (n+1)

def bfs():
    q = deque()
    q.append(1)

    while q:
        x = q.popleft()

        for nx in tree[x]:
            if parent[nx] == 0:
                parent[nx] = x
                q.append(nx)
        
bfs()

for i in range(2,n+1):
    print(parent[i])

