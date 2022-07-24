result = []
while True:
    stack = []
    a = input()
    flag = True
    if a == '.':
        break
    for i in a:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                temp = stack.pop()
                if temp != '(':
                    flag = False
                    break
            else:
                flag = False
                break
        elif i == ']':
            if stack:
                temp = stack.pop()
                if temp != '[':
                    flag = False
                    break
            else:
                flag = False
                break
    if flag and not stack:
        result.append('yes')
    else:
        result.append('no')

for r in result:
    print(r)
