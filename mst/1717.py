import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
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

for _ in range(m):
    f,a,b = map(int, input().split())

    if f == 0:
        union(a,b)
    else:
        x1 = find(a)
        x2 = find(b)

        if x1 == x2:
            print("YES")
        else:
            print('NO')
        
    