https://www.acmicpc.net/problem/2493

"""
방법을 생각하다가 완전탐색으로는 시간이 너무 오래걸릴거같아 힌트를 보게되었고 해결하였다.
힌트는 삭제하라였다.

즉 큰값이 아니면 stack에서 pop하는 방식을 통해 큰 값만 남기게 되고 큰값이 있어서 신호를 보낼 수 있으면 그 값으로하면되고 큰 값을 다 빼도 못한다면 0을 넣어주면된다./ 

"""

N = int(input())
arr = ([[i + 1, int(value)] for i, value in enumerate(input().split())])
stack = []
result = []
for i in range(N) :
    if len(stack) == 0 :
        stack.append(arr[i])
        result.append(0)
    else :
        while len(stack) >= 0 :
            if len(stack) == 0 :
                stack.append(arr[i])
                result.append(0)
                break
            if stack[-1][1] > arr[i][1] : # 더 클거나 같은경우 
                result.append(stack[-1][0])
                stack.append(arr[i])
                break
            else :
                stack.pop()

print(' '.join(map(str, result)))
