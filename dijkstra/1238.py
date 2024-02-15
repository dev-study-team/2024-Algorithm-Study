import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n,m,x = map(int, input().split())

graph = [[] for _ in range(m+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))



def dijkstra(start):
    q = []
    distance = [INF] * (m+1)
    
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
    return distance


_max = -INF
for i in range(1, n+1):
    go_party = dijkstra(i) # 각 집에서 파티로 가는 최단거리 
    back_home = dijkstra(x) # 파티에서 각 집으로 가는 최단거리
    _max = max(_max, go_party[x] + back_home[i])


print(_max)

