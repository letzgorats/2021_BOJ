def solution(n):
    answer = ''
    while n:
        if n % 3 != 0:  # 3의 배수가 아니라면,
            answer += str(n % 3)
            n //= 3 
        else:   # 3의 배수라면,
            answer += "4"
            n = n//3 - 1
    return answer[::-1]

def solution(n):
    if n <= 3:
        return '124'[n-1]
    elif n > 3:
        q,r = divmod(n-1,3)
        return solution(q) + '124'[r]

