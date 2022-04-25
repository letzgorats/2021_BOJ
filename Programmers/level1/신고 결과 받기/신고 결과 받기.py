## 1
- 20.8 / 100.0

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


## 2
- 87.5 / 100.0

def solution(id_list, report, k):
    answer = []
    report_set = set(report)
    how_many = {}
    answer = {}
    for i in id_list:
        if i not in how_many:
            how_many[i] = 0
            answer[i] = 0

    for r in report_set:
        a = r.split()[0]
        b = r.split()[1]
        how_many[b] += 1
        # if how_many[b] >= k:
    # print(how_many)
    
    for B,v in how_many.items():
        if v >= k:
            # print(B)
            for AB in report_set :
                # print(AB)
                if AB.split()[1] == B:
                    answer[AB.split()[0]] += 1
                    # print(answer)
    answer = list(answer.values())
    return answer

## 3
- 91.7 / 100.0

from collections import defaultdict 

def solution(id_list, report, k):
    
    report = list(set(report))  # 중복 제거
    # print(report)
    
    be_reported = defaultdict(int)
    real_stopped = []
    for singo in report:
        a = singo.split()[0]    # 신고자
        b = singo.split()[1]    # 신고당한 사람
        be_reported[b] += 1
        if be_reported[b] == k:
            real_stopped.append(b)
    # print(real_stopped)
    # print(be_reported)
    answer = [0] * len(id_list)
    
    for b in real_stopped:
        for a in report:
            if b == a.split()[1]:
                answer[id_list.index(a.split()[0])] += 1

    return answer

