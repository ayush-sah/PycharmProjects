ans = []
for _ in range(int(input())):
    __ = int(input())
    l = list(input())
    l.sort()
    while True:
        if len(l) == 0:
            ans.append("YES")
            break
        elif l[0] != l[1] or len(l) == 1:
            ans.append("NO")
            break
        else:
            l = l[2:]

for i in ans:
    print(i)