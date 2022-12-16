from collections import deque

def solution(maps):
    
    N = len(maps)   # 행
    M = len(maps[0])    # 열
    dr = [-1,1,0,0] # 행 - 상 하 좌 우 
    dc = [0,0,-1,1] # 열 - 상 하 좌 우
    
    answer = 0 
    
    def dfs(r,c):
        queue = deque([(r,c)])   # 시작 위치 (0,0)
        
        while queue:
            
            r, c = queue.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M: # 좌표가 범위 안에 들어오면
                    if maps[nr][nc] == 1: # 갈 수 있는 길이고, 방문하지 않은 길이라면,
                        # 방문하지 않은 리스트를 따로 만들어 줄 필요없이, 갈 수 있는 길의 값이 1이므로,
                        # 방문했다면 1은 아닐 것이다.
                        maps[nr][nc] = maps[r][c] + 1
                        queue.append((nr,nc))
            # print(queue,maps[r][c])
            
        return maps[N-1][M-1]
    
    
    answer = dfs(0,0)
    
    return -1 if answer == 1 else answer
