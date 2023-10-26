from collections import defaultdict
def solution(input_string):
    answer = ''
    
    alphabet = defaultdict(list)
    
    for idx,s in enumerate(input_string):
        alphabet[s].append(idx)
    
    for k,v in alphabet.items():
        
        distributed = 0
        
        if len(v) == 2:
            if ((v[0] + 1) != v[1]):
                answer += str(k)
        elif len(v) >= 2:
            for i in range(len(v)-1):
                if v[i+1] != v[i] + 1:
                    distributed += 1
            
            if distributed != 0:
                answer += str(k)

    answer = "".join(sorted(list(answer)))
           

    return "N" if answer == "" else answer
