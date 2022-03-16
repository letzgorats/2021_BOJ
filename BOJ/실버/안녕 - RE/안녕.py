import sys
input = sys.stdin.readline


N = int(input())

# 1번 사람부터 N번 사람까지의 잃는 체력 리스트
lose_hp = list(map(int,input().split()))
# 1번 사람부터 N번 사람까지의 얻는 기쁨 리스트
get_joy = list(map(int,input().split()))

lose_hp = [0] + lose_hp 
get_joy = [0] + get_joy

# 체력 0부터 100까지 N 명의 사람 
dp = [[0 for _ in range(101)] for _ in range(N+1)]

for i in range(1,N+1):  # 사람 수 
    for j in range(1,101):  # 체력을 늘려가면서 들어갈 수 있는지
        if j - lose_hp[i] > 0 : # 들어갈 수 있을 때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lose_hp[i]] + get_joy[i]) 
        else: 
            dp[i][j] = dp[i-1][j]

# print(dp)
print(dp[N][99])
