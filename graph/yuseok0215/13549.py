from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 100001


def bfs():

    q = deque()

    if n == 0:
        q.append(1)
    else:    
        q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            return visited[x]
        
        for nx in (x-1, x+1, 2*x):
            if 0<= nx < 100001 and visited[nx] == 0:
                if nx == 2*x:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)


if n == 0:
    print(bfs()+1)
else:
    print(bfs())