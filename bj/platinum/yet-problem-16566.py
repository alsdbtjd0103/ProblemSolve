#풀었지만  시간초과.. sort를 하면 안될 것 같다.

import sys
import math
input=sys.stdin.readline
n,m,k=map(int,input().rstrip().split())
card=list(map(int,input().rstrip().split()))
chul=list(map(int,input().rstrip().split()))
card.sort()
# n,m,k=10,7,5
# card=[2,5,3,7,8,4,9]
# card.sort()
# chul=[4,1,1,3,8]

start=0
end=m-1
loc=False
result=[]
for i in range(k):
    start,end=0,len(card)-1
    idx=(start+end)//2

    for j in range(m//2):
        idx=(start+end)//2

        # print('start: ',start,'end: ',end)
        # print("index: ",idx)

        elif start==idx or idx==0:
            if card[idx]<chul[i]:
                print(card[idx+1])
                card.remove(card[idx+1])
                break
            else:
                print(card[idx])
                card.remove(card[idx])
                break
        elif card[idx]>chul[i]:
            if card[idx-1]<=chul[i]:
                print(card[idx])
                card.remove(card[idx])
                break
            else:
                end=idx
                start=0
        elif card[idx]<chul[i]:
            start=idx
            end=len(card)-1     


    



    