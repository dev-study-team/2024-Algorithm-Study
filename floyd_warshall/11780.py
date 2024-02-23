# import sys
# input = sys.stdin.readline

# INF = 1e9

# n = int(input())
# m = int(input())
# graph = [[INF] * (n+1) for _ in range(n+1)]
# route = [[[] for _ in range(n+1)] for _ in range(n+1)]

# for _ in range(m):
#     a,b,c = map(int, input().split())
#     graph[a][b] = min(c, graph[a][b])


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         for k in range(1,n+1):
#             route[j][k].append(j)
#             if j==k:
#                 graph[j][k] = 0
#                 route[j][k].append(0)
#             if graph[j][k] > graph[j][i] + graph[i][k]:
#                 graph[j][k] = graph[j][i] + graph[i][k]
#                 route[j][k].append(i)
#             route[j][k].append(k)

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(graph[i][j], end=' ')
#     print()    

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(*route[i][j])
#     print()    


## 해답
import sys
input = sys.stdin.readline
INF = float("inf")

n = int(input())
m = int(input())
path = [[()]*(n+1) for _ in range(n+1)] # 최단 경로 리스트
APSP = [[INF]*(n+1) for _ in range(n+1)] # 최소 비용 리스트
for i in range(1, n+1):
    APSP[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    APSP[a][b] = min(APSP[a][b], c)
    path[a][b] = (a, b)
    
def floyd_warshall():
    for mid in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                cal_cost = APSP[i][mid] + APSP[mid][j]
                if cal_cost < APSP[i][j]:
                    APSP[i][j] = cal_cost
                    path[i][j] = path[i][mid] + path[mid][j][1:]
                    # 1 -> 4 1-> 2(1,2)  2-> 4(3,4) -> (1,2,3,4)
    return

floyd_warshall()

for i in range(1, n+1):
    line = []
    for j in range(1, n+1):
        if APSP[i][j] == INF:
            line.append(0)
        else:
            line.append(APSP[i][j])
    print(*line)

for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(path[i][j]), *path[i][j])