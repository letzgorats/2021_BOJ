## 풀이 1

import sys
input = sys.stdin.readline
 
M = int(input())
queue = set()
 
for _ in range(M):
    in_put = input().rstrip()
    if in_put == "all":
        queue.update([i for i in range(1,21)])
        # queue = set(i for i in range(1,21))
    elif in_put == "empty":
        queue = set()
    else:
        cmd = in_put.split()[0]	# 명령어
        number = int(in_put.split()[1])	# 숫자
 
        if cmd == "add":
            queue.add(number)
        elif cmd == "check":
            if number in queue:
                print(1)
            else:
                print(0)
        elif cmd == "remove":
            queue.discard(number)
        elif cmd == "toggle":
            if number in queue:
                queue.remove(number)
            else:
                queue.add(number)
                
## 풀이 2
import sys
input = sys.stdin.readline
 
from collections import deque
import heapq 
from itertools import permutations,combinations
 
M = int(input())
S = 0b0
 
for _ in range(M):
    in_put = input().rstrip()
    if in_put == "all":
        S = 0b111111111111111111111 # 0~20까지 총 21개의 1 (0자리는 무의미한 값)
        # print(queue)
    elif in_put == "empty":
        S = 0b000000000000000000000 # 0~20까지 총 21개의 0 (0자리는 무의미한 값)
    else:
        cmd = in_put.split()[0]
        number = int(in_put.split()[1])
    
        if cmd == "add":
            S = S | (1 << number)   # 원소 추가
        elif cmd == "check":
            if S & (1 << number) == (1<<number): # S&(1<<number) 만 해도 된다.
                print(1)
            else:
                print(0)
        elif cmd == "remove":
            S = S & ~(1 << number)  # 무조건 0을 만들어야 하니까 ~을 해주고 &를 해준다.
        elif cmd == "toggle":
            S = S ^ (1 << number)   # 다르면 1(추가해주고), 같으면 0(없애준다)
                
                
                
