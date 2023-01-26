import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 16   # 1<= N <= 15

dp[0] = 2
# 4, 9, 25
for i in range(1,N+1):
    dp[i] = (dp[i-1] + (dp[i-1] -1))
    # print(dp[i])

print(dp[N]**2)

# 규칙성을 찾자 dp
