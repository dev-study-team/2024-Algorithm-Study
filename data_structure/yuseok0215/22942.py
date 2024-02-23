# 원의 좌표의 범위를 가지고 풀어내려고 했었다. 하지만 그렇게 풀면 난이도가 너무 어려워지고 경우의 수를 따지기가 어려웠다.
# () 괄호로 원을 표현하여 (1  (2  )1  )2  이런식으로 겹치는 경우에 stack 남도록 하는 로직으로 풀어냈다.

import sys

N = int(sys.stdin.readline())
circles = []

for i in range(N):
    x, r = map(int, sys.stdin.readline().split())
    circles.append((x-r, i))
    circles.append((x+r, i))    
circles.sort() 

stack = []
for c in circles:
    if stack:
        if stack[-1][1] == c[1]:
        # 원이 겹치는 경우에는 이것이 성립하지 않는다.
        # 그러므로 pop을 정상적으로 하지 못해 결국 stack 값이 남게된다.
            stack.pop()
        else:
        # 스택에 있는 원이 현재 원이 아니라면
            stack.append(c)
    else: # 스택에 없을 때 일단 (좌표, 원 idx) 넣어준다.
        stack.append(c) 
    
if stack:
    print('NO')
else:
    print('YES')
