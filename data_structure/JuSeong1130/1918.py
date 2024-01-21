https://www.acmicpc.net/problem/1918
https://blog.naver.com/tipsware/222560727262

"""
내 생각
내생각이 중요하지 않았다.. 후위 표기법에 대해 아예 잘 못 생각하고 있었어서 풀수 없던 문제였다 ㅜㅜ

"""



# https://www.acmicpc.net/board/view/114981  https://www.acmicpc.net/board/view/101544
input_str = input()
result = []
operator = []

for word in input_str :
    if "A" <= word <= "Z" : # 문자일때 
        result.append(word)
    elif word == "(" : # ( 일때
        operator.append("(")
    elif word == ")" : # ) 일때
        while operator and operator[-1] != "(" :
            result.append(operator.pop())
        operator.pop()
    elif word == '*' or word == '/': 
        while operator and (operator[-1] == '*' or operator[-1] =='/'):  # * /가 앞에 있다면 그거 먼저 출력해줘야함 A*B/C는AB*C/이기때문 
            result.append(operator.pop())
        operator.append(word)
    elif word == '+' or word == '-':
        while operator and operator[-1] != '(': # + - 기준으로 오른쪽 왼쪽으로 나눠지기때문에 그전까지 있던 것은 모두 pop
            result.append(operator.pop())
        operator.append(word)
while operator :
    result.append(operator.pop())


print("".join(result))
        




    

    




# https://www.acmicpc.net/board/view/114981  https://www.acmicpc.net/board/view/101544
input_str = input()
result = []
operator = []

for word in input_str :
    if "A" <= word <= "Z" : # 문자일때 
        result.append(word)
    elif word == "(" : # ( 일때
        operator.append("(")
    elif word == ")" : # ) 일때
        while operator and operator[-1] != "(" :
            result.append(operator.pop())
        operator.pop()
    elif word == '*' or word == '/':
        while operator and (operator[-1] == '*' or operator[-1] =='/'):
            result.append(operator.pop())
        operator.append(word)
    elif word == '+' or word == '-':
        while operator and operator[-1] != '(':
            result.append(operator.pop())
        operator.append(word)
while operator :
    result.append(operator.pop())


print("".join(result))
        




    

    


