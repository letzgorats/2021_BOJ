import sys
input = sys.stdin.readline

K, P, N = map(int,input().split())

for _ in range(N):
    K = (K * P) % 1000000007   # 숫자가 커지면 연산시간이 오래걸려서 미리 나눠줘야 한다.
print(K)
