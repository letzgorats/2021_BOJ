def solution(n, times):
    
    answer = 0
    if n < len(times):  
        answer = min(times)
    else:
        left = 1
        right = max(times) * n
        while left <= right:
            mid = (left + right) // 2
            process = 0
            for t in times:
                process += mid // t
                # if process >= n:
                #     break
                    
            if n <= process:
                answer = mid
                right = mid -1
            elif n > process:
                left = mid + 1
        
        
    return answer
