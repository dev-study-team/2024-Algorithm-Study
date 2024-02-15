import sys
import heapq
input = sys.stdin.readline
INF = 1e9

v,e = map(int, input().split())
k = int(input())

distance = [INF] * (v+1)

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
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
    
dijkstra(k)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
        continue

    print(distance[i])


    