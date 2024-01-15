"""
여러번 봐줘야 하는 문제
count를 누적으로 이용해서 오름차순 순열을 표현했다
그리고 현재 숫자를 기준으로 푸쉬할만큼 하고 마지막 pop할 숫자가 현재 숫자와 일치하지 않으면
아예 못만든다는 사실을 인지하는 것이 필요했다.

43687521

43 6 87 521
9

1234 ++++
12 -- 
1256 ++
125 -
12578 ++
125 --
---

"""

count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num: # 제일 중요한 부분....
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