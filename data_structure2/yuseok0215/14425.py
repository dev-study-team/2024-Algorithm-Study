"""

"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr1 = []
for _ in range(n):
    arr1.append(input())

cnt  = 0
for _ in range(m):
    tmp = input()

    if tmp in arr1:
        cnt += 1

print(cnt)

