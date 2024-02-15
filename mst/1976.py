n = int(input())
m = int(input())

root = [i for i in range(n + 1)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]
    
def union(x,y):
    x = find(x)
    y = find(y)

    if y < x: # 값이 더 작은 쪽을 부모로
        root[x] = y
    else:
        root[y] = x

edges = []
for i in range(n):
    edges.append(list(map(int, input().split())))
    for j in range(n):
        if edges[i][j] == 1:
            union(i+1,j+1)

plan = list(map(int, input().split()))
plan_set = set(plan) # 중복 제거

check = find(root, plan[0])
for i in plan_set:
    if find(root, i) != check:
        print("NO")
        exit(0)
print("YES")


