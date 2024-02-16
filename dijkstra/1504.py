import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n,e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for n_idx, n_dist in graph[now]:
            if n_dist + dist < distance[n_idx]:
                distance[n_idx] = n_dist + dist
                heapq.heappush(q, (n_dist + dist, n_idx))
    return distance

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

result1 = d1[v1] + d2[v2] + d3[n]
result2=  d1[v2] + d3[v1] + d2[n]

_min = min(result1, result2)
if _min < INF:
    print(_min)
else:
    print(-1)



