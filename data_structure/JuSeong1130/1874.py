https://www.acmicpc.net/problem/1874

"""
스택에 넣었다 뺌으로써 어떤 수열이 만들어짐 단 push는 오름 차순을 지킴
임의의 수열이 주어질떄 이를 스택으로 만들 수 있는지를 묻는 문제

"""
from collections import deque

N = int(input())

arr = [int(input()) for _ in range(N)] # 입력받은 수열
arr = deque(arr)

result = []
nums = deque([i for i in range(1,N + 1)]) # 1부터 N까지 들어있는 값
stack = []

while len(arr) > 0 :
    if len(nums) > 0 and nums[0] <= arr[0]:
            result.append("+")
            stack.append(nums.popleft())
    else :
        # 현재값이 1인데 뽑으려는 값이 4이면 4까지 넣어준다
        # 이후 현재 값이 5인데 5보다 작으니 뽑아주면되는데 4는 당연히 넣어줬으니 뽑힐것이다.
        # 그런데 이미 들어있는 값중에서 예상되는 수열과 맞지 않으면 수열을 만들 수 없다.
        if (stack[-1] == arr[0]) : #스택 마지막 값과 뽑으려는 값이 일치하지 않으면 NO
            result.append("-")
            stack.pop()
            arr.popleft()
        else :
            print("NO")
            break
print(result)


"""
https://velog.io/@ny_/%EB%B0%B1%EC%A4%80-1874%EB%B2%88.-%EC%8A%A4%ED%83%9D-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
다른 사람풀이
내풀이와 다른 거는 아래는 1부터 N까지 값을 넣어놓지 않았고 나는 넣어놓은것


count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)











