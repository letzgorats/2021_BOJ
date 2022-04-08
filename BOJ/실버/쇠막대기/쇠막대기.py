import sys
input = sys.stdin.readline

cmd = input() # 괄호를 입력받는다.

stack = []  # stack을 선언하고

answer = 0
stack.append(cmd[0])  # stack에 맨처음 입력한 괄호를 집어넣고 시작한다.

for i in range(1,len(cmd)): # 1부터 cmd바로직전까지 돌면서(인덱스)
    if cmd[i] == "(":       # 해당 값이 '(' 면
        stack.append(cmd[i])  # stack에 집어넣고
    elif cmd[i] == ")":     # 해당 값이 ')'면
        if cmd[i-1] == "(":   # 바로 직전값이 '('였다면, 
            stack.pop()       # pop()을 해주고 (레이저니까)
            # 레이저 하나가 이등분하니까 *2를 해주고 
            answer += len(stack) * 2 
            # 아직 stack에 값이 있으니까 다음 레이저로 자를 때 중복해서 계산할 수 있으니 stack의 길이(쇠막대기 수)만큼 빼준다.
            answer -= len(stack)
        else:                 # 바로 직전값이 ')'였다면,
            stack.pop()       # stack에서 '('를 빼주고
            answer += 1       # ')'가 나와서 '('를 빼줬다는 것이 하나의 쇠막대기는 거기서 끝이 났다는 것이므로, + 1 을 해준다.  
print(answer)
