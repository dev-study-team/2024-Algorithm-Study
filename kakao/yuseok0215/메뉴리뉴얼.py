from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for i in course:
        arr = []
        for order in orders:
            for j in list(combinations(order, i)):
                joined_str = ''.join(sorted(j))
                arr.append(joined_str)
        sorted_arr = Counter(arr).most_common() 
        # 리스트 내 각 요소와 해당 횟수를 포함하는 튜플의 리스트를 반환하며, 횟수 기준으로 내림차순 정렬
        for menu, cnt in sorted_arr:
            if cnt > 1 and cnt == sorted_arr[0][1]:
            # 횟수가 2번이상 찍여야하고 가장 높은 횟수랑 같은 메뉴만 answer에 담겠다.
            # 근데 가장 높은 횟수인 menu가 2개이상일 수 있으니 탐색하는 것.
                answer.append(menu) 
                
    
    return sorted(answer)

# arr1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# arr2 = [2,3,4]	

# solution(arr1, arr2)