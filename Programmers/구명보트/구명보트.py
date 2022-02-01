def solution(people, limit):
    answer = 0
    standard = limit
    n = len(people)
    remove_list = []
    total = 0
    people = sorted(people,reverse=True)
    # print(people)
    while n!=0:
        remove_list.clear()
        standard = limit
        # print(standard)
        for p in people:
            if standard == 0:
                break
            if standard > 0:
                standard -= p
                if standard < 0 :
                    standard += p
                else:
                    total += 1
                    remove_list.append(p)
        n-= total
        total = 0
        # print(remove_list)
        
        for i in remove_list:
            people.remove(i)
        answer += 1
                
    return answer


from collections import deque

def solution(people, limit):
    answer = 0
    people = sorted(people)
    people = deque(people)
    print(people)
    while people:
        if len(people) >= 2:
            if people[0] + people[-1] <= limit :
                people.popleft() # 제일 가벼운 무게와
                people.pop() # 제일 큰 무게 하나씩
                answer += 1
            elif people[0] + people[-1] > limit :
                people.pop() # 제일 큰 무게만
                answer += 1
        else:
            answer += 1
            people.pop()
    return answer
