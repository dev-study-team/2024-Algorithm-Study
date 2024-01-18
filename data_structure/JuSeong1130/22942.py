https://www.acmicpc.net/problem/22942
https://velog.io/@leetaekyu2077/Python-%EB%B0%B1%EC%A4%80-22942%EB%B2%88-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B2%B4%EC%BB%A4


"""
내 생각
내생각으로는 N^2승이 되는 문제였고 고민하다 결국 힌트를 보게 되었다.

힌트는 괄호였다.
문제는 원이 교차되는 것이 없어야 하는 문제 였다. 
즉 원의 시작점과 끝점을 괄호라고 생각하고 이것이 A( B( A) B) 이렇게 되면 교차되는 문제기때문에 이를 이용해 풀어야 했다.
"""


import sys


N = int(sys.stdin.readline().rstrip())
arr = []


for i in range(N) :
    x, r = map(int, sys.stdin.readline().split()) # x는 위치 r은 반지름
    arr.append((x-r,i,0))
    arr.append((x+r,i,1))
arr.sort() # 튜플은 첫번째 원소를 기준으로 정렬해준다 이 문제에서 해결의 키이다.

stack = []
for i in range(len(arr)) :
    if len(stack) == 0 or arr[i][2] == 0:
        stack.append(arr[i])
    else :
        if stack[-1][1] == arr[i][1] :
            stack.pop()
        else :
            break

if not stack :
    print("YES")
else :
    print("NO")

다른사람 풀이
여기서는 stack이 있으면을 먼저 시작하고 i인덱스값 즉 위치값을 이용해 구현해낸다.
import sys

N = int(sys.stdin.readline())
circles = []

for i in range(N):
    x, r = map(int, sys.stdin.readline().split());
    circles.append((x-r, i))
    circles.append((x+r, i))    
circles.sort()

stk = []
for c in circles:
    if stk:
        if stk[-1][1] == c[1]: 
            stk.pop()
        else:
            stk.append(c)
    else:
        stk.append(c) 
    
if stk:
    print('NO')
else:
    print('YES')

https://velog.io/@leetaekyu2077/Python-%EB%B0%B1%EC%A4%80-22942%EB%B2%88-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B2%B4%EC%BB%A4
