"""

"""

n, m = map(int, input().split())

name = []
for i in range(1, n+1):
    name.append((i, input()))

print(name)

answer = []
for i in range(m):
    tmp = input()

    if tmp[0].isalpha():
        for j in range(m):
            if tmp == name[j][1]:
                answer.append(str(j+1))
                break
        continue
    
    int_tmp = int(tmp)
    answer.append(name[int_tmp-1][1])

for elem in answer:
    print(elem)