import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque([])

# 명령어 리스트
cmd_list = ['push', 'pop', 'size', 'empty', 'front', 'back']
for _ in range(N):
    cmd = input().strip()
    if cmd_list[0] in cmd :    # 명령어가 push일 때
        num = int(cmd.split()[1])
        queue.append(num)
    elif cmd == cmd_list[1] :   # 명령어가 pop일 때
        if len(queue) == 0:
            print(-1)
        else:
            num = queue.popleft()  # 가장 앞에 있는 정수 출력
            print(num)
    elif cmd == cmd_list[2] :   # 명령어가 size일 때
        print(len(queue))
    elif cmd == cmd_list[3] :   # 명령어가 empty일 때
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd == cmd_list[4] :   # 명령어가 front일 때
        if len(queue) == 0:
            print(-1)
        else:
            num = queue[0]  # 가장 앞에 있는 정수 출력
            print(num)
    elif cmd == cmd_list[5] :   # 명령어가 back일 때
        if len(queue) == 0:
            print(-1)
        else:
            num = queue[-1]  # 가장 뒤에 있는 정수 출력
            print(num)
