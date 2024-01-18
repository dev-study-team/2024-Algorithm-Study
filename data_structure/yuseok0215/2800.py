"""
설마 설마 했는데 진짜 콤비네이션을 사용했던 문제...


"""

from itertools import combinations

expr = list(input())
indices = []
stk = []
answers = set()

for i in range(len(expr)):
    if expr[i] == '(': 
        stk.append(i)
    elif expr[i] == ')': # 서로 쌍을 이루는 괄호의 index 쌍을 모은 리스트
        indices.append((stk.pop(), i))

for i in range(len(indices)):
    for comb in combinations(indices, i+1): # 조합의 길이가 1,2,3
        temp = expr[:] # 단순복사
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = "" # 빈문자를 삽입하는 이유는 index를 변하지 않게 하기 위함
        answers.add("".join(temp))      

for item in sorted(list(answers)):
    print(item)
