"""
스택을 이용해서 얼마나 append를 줄이는 것에 초점을 맞춰야했던 문제..

"""
import time
from collections import deque

start_time = time.time()

n = int(input())
tower_h = list(map(int, input().split()))

answer = [0] * n 
# answer을 빈배열로 놓고 append 하기보다는 0으로 초기값을 놓으면 
# 나중에 0을 넣기위해 시간을 쓰지 않아도 된다.
stack = []

for i in range(n):
    while stack:
        if tower_h[stack[-1][0]] < tower_h[i]: 
        # 현재 스택의 상위 높이보다 지금 타워 높이가 높으면
        # 스택의 상위 높이까지 레이저가 올 수 없다(오른쪽 타워가 더 높기 때문에)
            stack.pop()
        else: 
        # 현재 스택의 상위 높이보다 지금 타워 높이가 낮으면
        # 스택에 넣을 필요 없음 이미 쏘고 닿았기 때문
            answer[i] = stack[-1][0] + 1
            break
    stack.append((i, tower_h[i]))
    # if문에 걸렸기 때문에 더 높은 타워를 stack에 넣기
print(*answer)
end_time = time.time()
print("run time: ", end_time - start_time)


# 내 풀이
# start_time = time.time()

# n = int(input()) # 타워 개수
# tower_h = list(enumerate(map(int, input().split())))

# answer = [0] * n
# stack = []
# for i in range(n-1, 0, -1):
#     for t in stack:
#         if t[1] <= tower_h[i][1]:
#              answer[t[0]]=i+1
#              stack.pop() 

#     if tower_h[i][1] <= tower_h[i-1][1]:
#             answer[i] = tower_h[i-1][0] + 1
#     else:
#         stack.append(tower_h[i])


# for i in range(n):
#     print(answer[i], end=' ')

# end_time = time.time()
# print("run time: ", end_time - start_time)
    
        
        
    

    