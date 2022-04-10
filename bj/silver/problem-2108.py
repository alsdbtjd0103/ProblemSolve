import sys
input=sys.stdin.readline

def Aver(array):
  return round(sum(array)/len(array))

def Mid(array):
  array.sort()
  return array[len(array)//2]

def Most(array):
  count=[0 for i in range(0,8001)]
  array.sort()
  for i in array:
    count[i+4000]+=1
  max_index=[]
  max_value=max(count)
  for i in range(len(count)):
    if count[i]==max_value:
      max_index.append(i-4000)
  if len(max_index)==1:
    return max_index[0]
  else:
    return max_index[1]

def Range(array):
  return max(array)-min(array)
    

  
n=int(input())
arr=[]
for i in range(n):
  arr.append(int(input()))

print(Aver(arr))
print(Mid(arr))
print(Most(arr))
print(Range(arr))
