import sys
sys.setrecursionlimit(10**5)

n,m = map(int, input().split())

def backtracking(depth, temp):

    if len(temp) == m:
        print(*temp)
        return

    for i in range(1,n+1):
        if i not in temp:
            temp.append(i)
            backtracking(depth + 1, temp)
            temp.pop()

temp = []

backtracking(1, temp)