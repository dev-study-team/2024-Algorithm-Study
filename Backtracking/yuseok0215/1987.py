import sys
input = sys.stdin.readline

r,c = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(input()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def solution(x,y,cnt):
    global _max 
    
    _max = max(cnt, _max)

    if visited_alp == 'A-Z':
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<= nx < r and 0<= ny < c:
            if graph[nx][ny] not in visited_alp:
                visited_alp.append(graph[nx][ny])
                solution(nx,ny,cnt+1)
                visited_alp.pop()

visited_alp = [graph[0][0]]
_max = -1e9

solution(0,0,1)

print(_max)

## 답안 풀이 시간초과가 너무 많이 나서 로직만 연습하고 넘어가자
import sys

# bfs 풀이
# bfs
# def bfs():
#     global cnt
#     queue = set([(0, 0, graph[0][0])]) # 시간 초과를 줄이기 위해 중복되는 곳은 제거

#     while queue:
#         x, y, z = queue.pop()

#         # 말이 지날 수 있는 최대의 칸 초기화
#         cnt = max(cnt, len(z))

#         # 상/하/좌/우 탐색
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # 범위 내에 있고 알파벳이 중복이 안된다면 탐색
#             if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in z:
#                 queue.add((nx, ny, graph[nx][ny] + z))


# r, c = map(int, sys.stdin.readline().split())

# graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# cnt = 1

# bfs()
# print(cnt)