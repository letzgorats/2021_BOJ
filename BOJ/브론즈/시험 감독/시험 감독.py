n = int(input())    # 시험장 수 
aList = list(map(int,input().split())) # 각 시험장에 있는 응시자 수 
b, c = map(int,input().split()) # 총 감독관, 부 감독관

# 총 감독관은 1명만 있어야 함.
answer = n  # 총 감독관은 각 시험장마다 1명 필수 
left = []
for idx in range(n):  # 각 시험장에 있는 응시자 수에서 총 감독관이 감독할 수 있는 응시자 수만큼 빼준다.
    aList[idx] -= b 
    if aList[idx] > 0 : # 여전히 양수일 때만,
        left.append(aList[idx]) # left라는 리스트에 append
# -5 0 20 225 -9 13 14 91
# 20 225 13 14 91

for x in left:  # left를 돌면서 
    if x % c != 0 : # 나누어 떨어지지 않으면
        answer += x//c + 1  # 나눈 몫에다 + 1
    else: # 나누어 떨어지면
        answer += x//c # 몫만큼만 더해준다.

print(answer)
