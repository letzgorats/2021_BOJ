import sys
input = sys.stdin.readline

n, m, x, y, k = map(int,input().split())
# print(n,m,x,y,k)
board = []

for i in range(n):
    row = list(map(int,input().split()))
    board.append(row)
# print(graph)
cmd = list(map(int,input().split()))
# print(cmd)
dr = [0,0,-1,1] # 우 좌 상 하 (행)
dc = [1,-1,0,0] # 우 좌 상 하 (열)

dice = [0,0,0,0,0,0]    # 위 뒤 오른쪽 왼쪽 앞 아래

def go(cmd):
    
    a, b, c, d, e, f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]

    if cmd == 1 :    # 동    
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c

    elif cmd == 2:  # 서
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = c,b,f,a,e,d

    elif cmd == 3:  # 북
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = e,a,c,d,f,b
    
    elif cmd == 4:  # 남
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = b,f,c,d,a,e


nr, nc = x,y    # 시작 좌표
for i in cmd:
    # print(i)
    nr += dr[i-1]
    nc += dc[i-1]

    if nr < 0 or nr >= n or 0 > nc or nc >= m:
        nr -= dr[i-1]
        nc -= dc[i-1]
        continue
    go(i)
    if board[nr][nc] == 0:
        board[nr][nc] = dice[-1]
    else:
        dice[-1] = board[nr][nc]
        board[nr][nc] = 0

    print(dice[0])
