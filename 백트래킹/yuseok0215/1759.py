from itertools import combinations

l,c = map(int, input().split())
arr = list(map(str, input().split()))

comb = list(combinations(arr, l))

list_comb = [list(elem) for elem in comb]

def check(arr):
    global answer

    mo = 0
    ja = 0

    for alp in arr:
        if alp in ('a','e','i','o','u'):
            mo += 1
        else:
            ja += 1

    arr.sort()
    if mo >= 1 and ja >= 2:
        answer.append(''.join(arr))

answer = []

for elem in list_comb:
    check(elem)

answer.sort()
for elem in answer:
    print(elem)