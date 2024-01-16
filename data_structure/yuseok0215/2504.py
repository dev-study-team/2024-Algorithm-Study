# 스택의 성질을 잘 이용했어야 하는 문제

stack = [] # 스택
tmp = 1 # result에 더해주기 전 임시 변수
result = 0 # 결과 변수
p = list(input()) 

# 1~4번째 과정 시작
for i in range(len(p)):
  if p[i]=='(':
    tmp *= 2 
    stack.append(p[i])
    
  elif p[i]=='[':
    tmp *= 3
    stack.append(p[i])
    
  elif p[i]==')':
    if not stack or stack[-1]!='(': # 
      result = 0
      break
    if p[i-1]=='(': result += tmp
    tmp //= 2
    stack.pop() # stack에서 ( 삭제 결국 )을 append 하지 않기 때문에 () 같이 사라짐
    
  elif p[i]==']':
    if not stack or stack[-1]!='[':
      result = 0
      break
    if p[i-1]=='[': result += tmp
    tmp //= 3
    stack.pop()


# 결과 출력
if stack: # 열린 괄호가 더 많을 때
  print(0)
else:
  print(result)
