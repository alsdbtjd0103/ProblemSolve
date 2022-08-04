from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
tomato = []
initial = []
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    tomato.append(temp)

for a in range(h):
    for b in range(n):
        for c in range(m):
            if tomato[a][b][c] == 1:
                initial.append((a, b, c))


visited = [[[-1 for i in range(m)] for j in range(n)] for k in range(h)]

q = deque(initial)

d = [(1, 0, 0), [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
day = 0
while q:
    temp_h, x, y = q.popleft()
    if visited[temp_h][x][y] == -1:
        visited[temp_h][x][y] = 0
    for dx, dy, dh in d:
        nx, ny, nh = x+dx, y+dy, temp_h+dh
        if 0 <= nx < n and 0 <= ny < m and 0 <= nh < h:
            if visited[nh][nx][ny] == -1 and tomato[nh][nx][ny] == 0:
                visited[nh][nx][ny] = visited[temp_h][x][y]+1
                tomato[nh][nx][ny] = 1
                if day < visited[nh][nx][ny]:
                    day = visited[nh][nx][ny]
                q.append((nh, nx, ny))
flag = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                flag = False
                break
        if not flag:
            break
    if not flag:
        break
if flag:
    print(day)
else:
    print(-1)
