from collections import deque

n = int(input())

q = deque()
graph = []
shark_x, shark_y = 0, 0

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 9:
            shark_x, shark_y = i,j
    graph.append(temp)

dx = [0,0,-1,1]
dy = [-1,1,0,0]



# 먹을 수 있는 물고기에 대한 탐색
# 물고기를 찾을 수 있으면 grpah = 1 

def bfs(a, b,shark_size):
    q = deque()
    q.append((a, b))

    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    cand = []

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] <= shark_size and visited[nx][ny] == 1: #이동이 가능하면
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    q.append([nx,ny])

                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0: #물고기가 있고 그걸 먹을 수 있다면
                        cand.append([nx ,ny,distance[nx][ny]])

    cand_sorted = sorted(cand, key=lambda x:(x[2], x[0], x[1]))
    return cand_sorted

time = 0
shark = 2
eating = 0
while True:
    cand = bfs(shark_x, shark_y,shark)

    if len(cand) == 0 :
        break

    shark_x, shark_y, dist = cand[0]
    
    time += dist
    eating += 1

    if shark == eating:
        shark += 1
        eating = 0

    graph[shark_x][shark_y] = 0

print(time)