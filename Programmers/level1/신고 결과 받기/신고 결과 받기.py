from collections import defaultdict

def solution(id_list, report, k):
    user_and_attacked = defaultdict(int)    # 사용자와 신고당한 사용자
    answer = defaultdict(int)   # answer
    
    for id in id_list:  # id_list를 돌면서 각 id에 해당하는 value값을 0으로 설정
        answer[id] = 0
    # print(answer)
        
    for a_to_b in report :
        if a_to_b in user_and_attacked : pass
        else:
            user_and_attacked[a_to_b] += 1
    # print(user_and_attacked)
    mail = []
    
    for idx,id in enumerate(id_list):
        for a_to_b in user_and_attacked:
            if id == a_to_b.split()[1]:
                answer[id] += 1
                if answer[id] >= k:
                    mail.append(id)
    # print(answer)
    # print(mail)
    real_answer = defaultdict(int)
    for id in id_list:
        real_answer[id] = 0
        
    
    for id in mail:
        for j in user_and_attacked:
            if id == j.split()[1]:
                real_answer[j.split()[0]] += 1
    
    return list(real_answer.values())
