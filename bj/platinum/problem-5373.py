from collections import deque

cube=[[["r"]*3 for _ in range(3)] for i in range(6)]

color=["w","b","y","g","r","o"]
#윗 오른쪽 아래 왼쪽 앞 뒤
for i in range(len(cube)):
    for j in range(len(cube[i])):
        for k in range(len(cube[i][j])):
            cube[i][j][k]=color[i]
            
            
print(cube)
      