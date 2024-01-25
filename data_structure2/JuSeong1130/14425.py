사전을 이용해 개수를 구하면 되는 문제였다.

import sys

N,M = map(int,sys.stdin.readline().split()) # 문자열 개수 N,  검사해야 하는 개수 M

d = dict()
for i in range(N) :
    d[sys.stdin.readline().rstrip()] = 1

result = 0
for i in range(M) :
    if sys.stdin.readline().rstrip() in d :
        result += 1

print(result)

