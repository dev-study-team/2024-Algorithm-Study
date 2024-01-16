https://www.acmicpc.net/problem/2800


"""
내 생각
문제를 읽다보니 괄호가 제거가 된 조합을 뽑아내는 것 같아 조합으로 풀면 쉽겠다 생각하였다.

어려웠던점
1. 조합 라이브러리를 처음 사용하다보니 어려웠다 조합은 튜플로 나온다 ([3, 5],), ([0, 6],)
2. 값을 삭제하는 방식을 del을 사용하다보니 인덱스가 변경되는 문제가 있었다. 그런데 쉬웠다 = ""로 바꿔주면되는 문제였다.
3. 또한 ((2))는 (2)가 중복되어 나타난다. 문제에서는 서로 다른 식의 개수를 구한다 그래서 set을 이용해야했다.
"""


from itertools import combinations
# input_arr = [ [i, value] for i, value in enumerate(input())]
original_string = input()


stack = []
bracket_location = []
result = set()

for i in range(len(original_string)) :
    if original_string[i] == "(" :
        stack.append(i)
    elif original_string[i] == ")" :
        bracket_location.append([stack.pop(), i])

for i in range(1, len(bracket_location) +1) :
    combi = combinations(bracket_location, i) # combinations을 통해 모든 경우의 수를 확인
    for combi_list in combi :
        original_list = list(original_string)
        for k in combi_list :
            original_list[k[0]] = ""
            original_list[k[1]] = ""
        result.add(''.join(original_list))


for ans in sorted(list(result)):
    print(ans)


"""
2개일때 
2개 모두 한 경우
한개만 삭제한경우

"""

