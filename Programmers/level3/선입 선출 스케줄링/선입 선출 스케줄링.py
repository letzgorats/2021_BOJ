def solution(n, cores):
    
    answer = 0
    
    if n <= len(cores):
        answer = n
    else:
        n -= len(cores) # 처음 len(cores)개의 작업이 cpu에 들어갑니다.
        # start 는 1
        # end 는 코어들이 무조건 이 시간안에는 끝나는 시간
        start =  1
        end = max(cores) * n
        
        while start < end:	# start가 end와 같아지면 while문 탈출
        
            mid = (start + end) // 2    # 중간 위치
            process = 0
            
            # 시간 당 수행하게 되는 프로세스의 갯수는 시간의 약수인 작업시간을 갖는 cpu들의 합임.
            # 이를 이용하여 mid시간까지 수행한 프로세스의 갯수가 n보다 크거나 같은 지점을 찾고, 
            # 남은 만큼을 순회하며 마지막 cpu를 찾습니다.
            
            for core in cores:
                process += mid // core	# process는 mid시간까지 처리할 수 있는 총 작업개수
            
            if process >= n:	# process가 n보다 크거나 같으면, end를 mid 로 줄여야 함
                end = mid	
            else:		# process가 n보다 작으면, start를 mid+1 로 늘려야 함
                start = mid+1
            
        for core in cores:
        	n-= (end-1) //core		# (end-1)시간까지의 진행된 총 작업수를 구하고 전체 n에서 뺀다.  
    
        for i in range(len(cores)):
            if end%cores[i]==0:		# end시간의 약수에 cores[i]가 포함된다면,
                n-=1				# 남은 작업 -1 ( 작업 할당)
                if n==0:			# 작업이 비로소 0 이 됐다면,
                    answer = i+1	# 해당 코어번호가 답(+1을 한 이유는 인덱싱이 0부터이므로)
                    break
    
    return answer
