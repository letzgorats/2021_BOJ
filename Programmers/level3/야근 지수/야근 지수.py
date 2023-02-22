# 효율성 테스트 케이스 통과 못했지만, 정확성 테스트 케이스는 다 통과한 풀이 -- 70/100

import heapq

def solution(n, works):

    answer = 0
    
    if sum(works) <= n:
        return answer
    else:
        works = sorted(works,reverse = True)
        while n > 0 :
            n -= 1
            works[0] -= 1
            works = sorted(works,reverse = True)

        for w in works:
            answer += w**2
    
        return answer


# 효율성 테스트 케이스와 정확성 테스트 케이스 모두 다 통과한 풀이 -- 100/100


import heapq

def solution(n, works):
    
    q = []
    answer = 0 
    
    if sum(works) <= n:
        return answer

    else:
        for w in works:
            heapq.heappush(q,(-w,w))    # (-w,w)를 사용해 최대힙이 되도록 만들었다.

        while n != 0:
            a = heapq.heappop(q)[1]      # 진짜 원소(w)는 0번째가 아니라 1번째에 있으니까
            a -= 1
            heapq.heappush(q,(-a,a))
            n -= 1

        while q:
            element = heapq.heappop(q)[1] # 진짜 원소(w)는 0번째가 아니라 1번째에 있으니까
            # print(element)
            answer += (element ** 2)

        return answer

