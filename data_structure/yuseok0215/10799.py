import sys

input = sys.stdin.readline

str = input()

cut_cnt = 0
stick = 0


i = 0
while i < len(str):
    if str[i] == '(' and str[i+1] == ')': # 레이저가 있을 때
        cut_cnt += stick # 현재까지 막대기 개수만큼 더해준다.
        i += 2 # 레이저 건너뛰기
        continue
    elif str[i] == '(': # 막대기가 새로 시작될 떼
        stick += 1 
    elif str[i] == ')': # 막대기가 끝날 때
        stick -= 1
        cut_cnt += 1 # 막대기가 끝났다면 레이저 기준으로 잘려진 남은 부분

    i+=1
    
print(cut_cnt)

# 올바른 풀이법 (스택)
"""
ir= input()
stack=[]
cnt = 0
for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")
    else :
        if ir[i-1]=="(":
            stack.pop()
            cnt+=len(stack) # 첫 번째 경우인 현재의 쇠막대기들을 카운팅합니다.
            
        else :
            stack.pop()
            cnt+=1 # 이 부분은 두 번째 경우인 나머지 부분을 세는 것입니다.
print(cnt)
"""