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
    else : 
        stack.append(input_str.pop())
if success  == False or "(" in stack or "[" in stack:
    print(0)
else :
    print(sum(stack))

    




