# dfs 풀이 

import sys
input = sys.stdin.readline

def dfs(r,c):
    if 0 > r or r >= N or 0 > c or c >= N:
        return False
    if board[r][c] == 1:
        cnt.append(1)
        board[r][c] = 0 # 방문처리
        dfs(r-1,c)  # 북
        dfs(r,c+1)    # 동
        dfs(r+1,c)    # 남 
        dfs(r,c-1)  # 서
        return True
    return False


N = int(input().strip())
board = []
for _ in range(N):
    board.append(list(map(int,input().strip())))

answer_list = []
cnt = []
area = 0 
for r in range(N):
    for c in range(N):
        if dfs(r,c) == True:
            area += 1         
            answer_list.append(len(cnt))
            cnt = []
print(area)
for a in sorted(answer_list):
    print(a)
