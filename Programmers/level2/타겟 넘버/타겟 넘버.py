# BFS 로 푸는 방법

def solution(numbers, target):
    answer = 0 
    idx = 0
    n = len(numbers)
    queue = [[numbers[0],0] , [-numbers[0],0]]  # + - 
    
    while queue:
        temp,idx= queue.pop()
        idx += 1
        if idx < n :
            queue.append([temp + numbers[idx],idx])
            queue.append([temp - numbers[idx],idx])
        else:
            if temp == target :
                answer += 1
    return answer



# DFS 로 푸는 방법
def solution(numbers, target):
    
    idx = 0 
    answer = 0
    n = len(numbers)
    def dfs(idx,results):
         
        if idx < n:
            dfs(idx+1,results + numbers[idx])
            dfs(idx+1,results - numbers[idx])
        else:
            nonlocal answer
            if target == results:
                answer += 1
            return 
    dfs(0,0)
    
    return answer
