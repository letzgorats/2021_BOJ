import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    answer = 0 
    for num in range(N,M+1):
        for zero in str(num):
            if zero=='0':
                answer += 1
    print(answer)
