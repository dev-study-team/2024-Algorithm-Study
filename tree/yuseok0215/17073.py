import sys
input = sys.stdin.readline

n, w = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(2,n+1): # 루트노드는 제외한다..!
    if len(graph[i]) == 1:
        cnt += 1

print(w / cnt)
