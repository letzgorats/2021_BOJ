# 정확성 테스트 하나 빼고 다 맞은 풀이 - 너무 복잡하게 풀었다. - 계수정렬로 풀어보자 내일
from itertools import combinations, permutations

def solution(clothes):
    clothes = sorted(clothes,key = lambda x:x[1])
    category = []
    answer = 0
    current = clothes[0][1] # 가장 첫 의상종류부터 시작
    current_total = 0
    for i in range(len(clothes)):
        if current == clothes[i][1]:
            current_total += 1
        else:
            category.append(current_total)
            current_total = 1
            current = clothes[i][1]
    category.append(current_total) # 마지막 의상 종류 개수까지 append
    # print(category)
    answer += sum(category)
    n = len(category)
    combi = []
    for i in range(2,n+1):
        combi.append(list(combinations(category, i)))
    # print(combi)
    for x in combi:
        for i in x:
            now = 1
            for j in i:
                now *= j
            answer += now
    
    return answer


# 작년에도 (백준-패션왕 신해빈 문제랑 똑같은 문제) 풀었던 문제다. 해쉬 생각하니까 풀린다.

def solution(clothes):
    answer = 1
    category = {}
    clothes = sorted(clothes,key = lambda x : x[1])
    print(clothes)
    for x in clothes:
        if x[1] in category:
            category[x[1]] += 1
        else:
            category[x[1]] = 1
    # print(category)
    count_list = []
    for i in category.values():
        count_list.append(i)
    # print(count_list)
    for i in count_list:
        answer *= (i+1)
    answer -= 1 
    return answer
