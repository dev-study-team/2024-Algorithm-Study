# https://www.acmicpc.net/problem/2164

"""
1. 어떤생각으로 풀었는지

그냥 deque 이용해서 풀면 되겠다 생각함

어려웠던점
이슈
X

"""
from collections import deque

N = int(input())
arr = [i for i in range(1,N+1)]
dq = deque(arr)

while len(dq) != 1 :
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())
