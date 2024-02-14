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


def bfs(x_shark,y_shark):

    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((x_shark,y_shark))
    cand = [] # 먹을 수 있는 물고기의 후보군을 담아준다.

    visited[x_shark][y_shark] = 1 # 자기 자리 방문

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if graph[nx][ny] < graph[x_shark][y_shark] and graph[nx][ny] != 0:
                    visited[nx][ny] = visited[x][y] + 1
                    cand.append([visited[nx][ny] - 1, nx, ny]) 
                    # 먹을 수 있는 물고기를 만났을 때 후보를 저장한다.
                elif graph[nx][ny] == graph[x_shark][y_shark]: 
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

    return sorted(cand, key = lambda x:(x[0], x[1], x[2]))

cnt = 0
size = [2,0]
while True:
    graph[shark_x][shark_y] = size[0]
    cand = deque(bfs(shark_x, shark_y))

    if not cand: # 먹을 수 있는 고기 X
        break

    move_cnt, x, y = cand.popleft()
    cnt += move_cnt
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    graph[shark_x][shark_y] = 0
    shark_x, shark_y = x,y

print(cnt)
