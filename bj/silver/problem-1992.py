import sys
input = sys.stdin.readline
n = int(input())
pic = [list(map(str, input().rstrip())) for i in range(n)]


def divAndCon(x, y, N):
    result = pic[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if result != pic[i][j]:
                print("(", end='')
                divAndCon(x, y, N//2)
                divAndCon(x, y+N//2, N//2)
                divAndCon(x+N//2, y, N//2)
                divAndCon(x+N//2, y+N//2, N//2)
                print(")", end='')
                return
    print(result, end='')


divAndCon(0, 0, n)
