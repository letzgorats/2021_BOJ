import sys
input = sys.stdin.readline

s = input().strip()
bracket = []
answer = 0
tmp = 1

# for i in s: 말고 인덱스형식으로 접근해야 한다.
for i in range(len(s)):
    if s[i] == "(":
        tmp *= 2
        bracket.append(s[i])

    elif s[i] == "[":
        tmp *=3
        bracket.append(s[i])
        
    elif s[i] == ")":
        # bracket이 비어있거나 짝이 안맞는 쌍일 경우 올바르지 않은 괄호문자열 
        if len(bracket) == 0 or bracket[-1] == "[":
            answer = 0 
            break
        # 직전의 괄호가 '('으로 쌍이 맞을 때만 answer에 tmp저장
        if s[i-1] == "(":
            answer += tmp
        tmp //= 2
        bracket.pop()
    
    elif s[i] == "]":
        if len(bracket) == 0 or bracket[-1] == "(":
            answer = 0 
            break
        # 직전의 괄호가 '['으로 쌍이 맞을 때만 answer에 tmp저장
        if s[i-1] == "[":
            answer += tmp
        
        tmp //= 3
        bracket.pop()

if bracket:
    print(0)
else:
    print(answer)
