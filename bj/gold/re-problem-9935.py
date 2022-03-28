# 처음에는 스택 사용안하고 replace 이용해서 했는데 이러면 시간초과가 발생한다.
# 이 문제는 스택을 이용해서 지금 들어온 문자가 boom의 마지막 글자와 같으면
# 바로 스택안을 검사해서 boom이면 pop한다.
# 이렇게하면 단시간내에 검사가능하다.
# 마지막 글자와 비교한다는 아이디어가 필요한 거 같다.

arr=input()
boom=input()
stack=[]
last=boom[-1]
for i in arr:
    stack.append(i)
    if i==last:
        if ''.join(stack[-len(boom):])==boom:
            del stack[-len(boom):]
    

            

if not stack:
    print("FRULA")
else:
    print(''.join(stack))
