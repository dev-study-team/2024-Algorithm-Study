"""
실수
1. pop을 하고 담은 값을 이용해야했는데 pop해서 값을 비교하다보니 인덱스가 이상해졌다
2. ( 만들어 오는경우, )만들어오는경우 예외처리를 해주어야했다. 백준을 보니 최소값 아니면 최대값일때를 가정하고 값을 넣어보라 추천했다
3. 타입이 명시적이지 않아 힘들다..

생각
( [ 는 넣고
) ] 는 두가지 상황이 존재하며 뒤에 들어있는 값을 뺴오기 위해 pop을 이용하면 됬다.
1. 앞이 숫자라면 
이경우는 res라는 값을 업데이트 해주면된다.
2. 앞이 ( [ 라면 
이경우는 값을 계산해서 넣어주면된다.

예외 주의 사항
1. ( 만 있는 상황 ) 만 있는 상황
2. ) ] 가 들어왔는데 len가 없는 상황 pop할때 오류나서안됨

"""
from collections import deque

input_str = deque(input())
stack = deque()
result = 0
success = True

length = len(input_str)
for i in range(length) :
    if success == False :
        break
    findStr = input_str.popleft()
    if findStr == "(" :
        stack.append("(")
    elif findStr == "[" :
        stack.append("[")

    elif findStr == ")" :
        res = 0
        while True :
            if(len(stack) == 0) :
                success = False
                break
            num = stack.pop()
            if num == "[" :
                success = False
                break
            if num == "(" :
                if(res == 0) :
                    res = 2
                stack.append(res)
                break
            res += 2 * int(num)
    elif findStr == "]" :
        res = 0
        while True :
            if(len(stack) == 0) :
                success = False
                break
            num = stack.pop()
            if num == "(" :
                success = False
                break
            if num == "[" :
                if res == 0 :
                    res = 3
                stack.append(res)
                break                
            res += 3 * int(num)
if success  == False or "(" in stack or "[" in stack:
    print(0)
else :
    print(sum(stack))


다른 사람 코드

이문제의 풀이 방식은 (가 나오면 2를 곱하고 [ 가나오면 3을 곱하고] 가나오면 3을 나누고 )가 나오면 2를 나눠 구하는 문제이다.

(()[[]]) 의 경우 
2 * 2  앞에 있는 값은 4가 되고 이후 result에 값을 넣은 다음에 () = 2는 계산됬으니 2를 나눠준다.
그리고 ( [ [ 2 * 3 * 3 이 되는데 ]가 나올때 그리고 []가 완성됬을때 값을 계산해 넣어준다 뒤에 있는 ]는 앞에]가 나오면 값을 넣어주지 않는다 이미 앞에서 계산된 값이 들어갔기 때문이다.
즉 (2 * 2) + (2 * 9)가 되게 만들면된다 어렵다..

일단 //2 //3 다시 나눠줘야 하는 것이 잘 이해가 되지 않았고
두번쨰로 ()나 []가 완성됬을때 해줘야하는지도 단번에 이해가 되지 않았다. 지금이야 풀이방식이 이해가지만 어렵다..


stack = [] # 스택
res = 1 # result에 더해주기 전 임시 변수
result = 0 # 결과 변수
p = list(input()) # 입력값

# 1~4번째 과정 시작
for i in range(len(p)):
  if p[i]=='(':
    res *= 2
    stack.append(p[i])
    
  elif p[i]=='[':
    res *= 3
    stack.append(p[i])
    
  elif p[i]==')':
    if not stack or stack[-1]!='(':
      result = 0
      break
    if p[i-1]=='(': result += res
    res //= 2
    stack.pop()
    
  elif p[i]==']':
    if not stack or stack[-1]!='[':
      result = 0
      break
    if p[i-1]=='[': # 이문제의 키는 여기다 [[]]의경우 맨마지막 ]는 전이 ]이니 계산되지않는다 즉 앞에서 계산됬으니 계산하지 않는것
        result += res
    res //= 3
    stack.pop()


# 결과 출력
if stack: # stack에 값이 들어있는 경우 ( [ 인경
  print(0)
else:
  print(result)





    




