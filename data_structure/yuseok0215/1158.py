n,k = map(int, input().split())

cir = [i for i in range(1,n+1)]

remove_idx = 0

ans = []
while len(cir) != 0:
    remove_idx += k-1
    remove_idx %= len(cir)
    ans.append(cir.pop(remove_idx))


print('<', end='')
for i in range(n-1):
    print(str(ans[i])+', ', end='')
print(str(ans[-1]) + '>')
    

