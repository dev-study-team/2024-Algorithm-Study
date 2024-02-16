import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

a,b = map(int, input().split())

distance = [INF] * (n+1)
prev_node = [0] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for idx, n_dist in graph[now]:
            if distance[idx] > n_dist + dist:
                distance[idx] = n_dist + dist
                prev_node[idx] = now
                heapq.heappush(q, (n_dist + dist, idx))

dijkstra(a)
print(distance[b])

path = [b]
now = b

while now != a:
    now = prev_node[now]
    path.append(now)
    
path.reverse()

print(len(path))
print(' '.join(map(str, path)))
