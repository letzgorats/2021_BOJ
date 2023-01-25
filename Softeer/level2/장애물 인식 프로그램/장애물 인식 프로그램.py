# BFS로 푸는 풀이

import sys
from collections import deque
input = sys.stdin.readline

def bfs(r,c,visited):
    global area
    area = 1
    visited[r][c] = True
    dq = deque()
    dq.append([r,c])
    while dq:
        r,c = dq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<= nr < N and 0<=nc < N:
                if visited[nr][nc]==False and board[nr][nc] == 1 :
                    area += 1
                    visited[nr][nc] = True
                    dq.append([nr,nc])
                    
    answer_list.append(area)



N = int(input())
board = []
dr = [0,0,1,-1] # 동 서 남 북
dc = [1,-1,0,0]
visited = [[False] * N for _ in range(N)]

for _ in range(N):
    board.append(list(map(int,input().strip())))

answer_list = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == False and board[i][j] == 1:
            bfs(i,j,visited)

print(len(answer_list))
for a in sorted(answer_list):
    print(a)
