n=int(input())
a=list(map(int,input().split()))
tree=[[] for i in range(n)]
for i in range(n):
    if a[i]==-1:
        continue
    tree[a[i]].append(i)

k=int(input())
remove_node = [k]

def dfs(s):
    for a in tree[s]:
        if a not in remove_node:
            remove_node.append(a)
            dfs(a)
dfs(k)

for r in remove_node:
    tree[r]=[-1]
    for i in range(n):
        if r in tree[i]:
            tree[i].remove(r)

answer=0
for t in tree:
    if len(t)==0:
        answer+=1
print(answer)
