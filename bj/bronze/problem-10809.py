s=input()
alpha=[0 for _ in range(26)]
for i in range(26):
    if alpha[i]==0:
        idx=s.find(chr(i+97))
        if idx!=-1:
            alpha[i]=idx
        else:
            alpha[i]=-1
for i in alpha:
    print(i,end=' ')
        
    
