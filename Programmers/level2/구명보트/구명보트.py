# 처음에 최대 2명을 태울 것이라는 고려하지 않고 풀었던 풀이와, 효율성을 체크하지 않았던 풀이
def solution(people, limit):
    answer = 0
    standard = limit  # standard라는 변수에 기존 limit 저장
    n = len(people) # n이라는 변수에 people 리스트의 길이 저장(사람 수)
    remove_list = []    # remove_list 라는 빈 리스트 생성(태울 사람을 임시로 저장하는 리스트)
    total = 0   # total이라는 변수 ( 이 변수는 내가 최대 2명을 태울 것이라는 것을 못보고 한번에 태울 수 있는 사람 수를 저장하기 위해 변수를 잡음)
    people = sorted(people,reverse=True)    # people을 내림차순으로 정렬
   
    while n!=0: # n이 0이 될 때까지(무인도의 사람을 다 태울 때까지)
        remove_list.clear() # 태울사람을 임시로 저장하는 리스트는 다시 clear
        standard = limit  # standard는 다시 limit으로 초기화
    
        for p in people:    # 내림차순으로 정렬된 people 리스트를 돌면서 
            if standard == 0:   # standard가 0이 되면 
                break   # 빠져나온다
            if standard > 0:    # standard가 양수이면(아직 태울 수 있는 사람이 있을 수 있는 조건)
                standard -= p   # standard에 우선 지금 for문을 통해 돌고 있는 사람 무게(p)를 빼주고
                if standard < 0 :   # 음수라면
                    standard += p   # 다시 복구
                else:   # 여전히 0보다 크거나 같다면
                    total += 1  # 그 사람은 태울 수 있는 것(total += 1)
                    remove_list.append(p)   # remove_list에도 그 사람을 추가해준다.
        n-= total   # limit을 기준으로 total 수 만큼의 사람을 태울 수 있으니까 총 사람수인 n에서 total을 빼준다.
        total = 0   # total을 다시 0으로 초기화
        
        for i in remove_list:   # remove_list를 돌면서 포함되어있는 사람을  
            people.remove(i)    # people 리스트에서 제거해준다.
        answer += 1 # answer은 한번 보트를 태운 횟수를 뜻함 +1
                
    return answer


# 제대로 된 풀이
from collections import deque 

def solution(people, limit):
    answer = 0
    people = sorted(people) # people을 오름차순으로 정렬한다.
    people = deque(people)  # people 리스트를 deque화 시킨다
    
    while people:   # people리스트에 사람이 다 빌 때까지 while문을 돈다.
        if len(people) >= 2:    # 현재 people리스트에 사람이 최소 2명 이상이라면
            if people[0] + people[-1] <= limit :    # 현재 people 리스트의 첫 원소(가장 가벼운 무게)와 마지막 원소(가장 무거운 무게)의 합이 limit보다 작거나 같으면  
                people.popleft() # 제일 가벼운 무게와
                people.pop() # 제일 큰 무게 하나씩 pop해준다
                answer += 1 # 태울 수 있는 횟수 1 증가 
            elif people[0] + people[-1] > limit :   # limit보다 크면, 가장 작은 무게가 더해져서 limit을 넘어버린 것이므로,  
                people.pop() # 제일 큰 무게만 pop해준다.(무인도에는 limit보다 작은 무게만큼의 사람만 존재한다.)
                answer += 1 # 태울 수 있는 횟수 1 증가
        else:   # 현재 people 리스트에 사람이 1명이라면,
            answer += 1 # 그냥 태우고 와야 하므로 횟수 1 증가 
            people.pop()    # 나머지 그 사람도 people 리스트에서 제거
    
    # while문 다 빠져나오면 answer 리턴
    return answer
