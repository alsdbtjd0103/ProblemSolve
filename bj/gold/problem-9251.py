a=list(input())
b=list(input())
a_len=len(a)
b_len=len(b)
length=max(a_len,b_len)
d=[0]*length    # 인덱스까지의 최장 부분수열의 길이
if a_len>=b_len:
    for i in range(a_len):
        for j in range(b_len):
            if a[i]==b[j]:
                d[j]+=1
            else:
                
                