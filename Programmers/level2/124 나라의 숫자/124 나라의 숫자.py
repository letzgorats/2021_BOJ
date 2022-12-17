import itertools

def solution(n):
    answer = ''
    sets = "124"
    
    if n <= 3:
        if n == 1: answer = 1
        elif n == 2 : answer = 2
        else: answer = 4
    
    elif n > 3:
        exponent = 0
        tmp = 0
        for i in range(1,n):
            tmp += 3 ** i
            if tmp > n :
                tmp -= 3** i
                exponent = i
                break
        
        tmp_share = n // tmp 
        tmp_mod = n % tmp
        data = itertools.product(sets, repeat = exponent)
    
        for idx,x in enumerate(data):
            if idx == tmp_mod -1:
                answer = ''.join(x)
                break
                # print(x,answer)
        # answer = data[tmp_mod-1]
        # print(tmp_share, tmp_mod)
        # print(answer)
    return str(answer)
