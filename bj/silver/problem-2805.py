import sys
sys.setrecursionlimit(10000000)


def bi_search(start, end, num):
    temp = 0
    mid = (start+end)//2

    for i in h:
        temp += max(0, i-mid)
    if start > end:
        return mid
    if temp >= num:
        return bi_search(mid+1, end, num)
    elif temp < num:
        return bi_search(start, mid-1, num)


input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
h = list(map(int, input().rstrip().split()))
print(bi_search(1, max(h), m))
