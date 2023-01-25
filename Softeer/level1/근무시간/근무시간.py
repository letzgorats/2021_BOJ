import sys
input = sys.stdin.readline

answer = 0
for _ in range(5):
    start, finish = map(str,input().split())
    f = list(finish.split(":"))
    s = list(start.split(":"))

    answer += (int(f[0]) * 60 + int(f[1])) - (int(s[0]) * 60 + int(s[1]))

print(answer) 


# 시간을 먼저 분으로 계산 + 나머지 분 = 총 분

# 6:01 ~ 9:00 라고 하면, 900-601 = 299 가 나와서 잘못된 분수로 계산될 수 있기 때문에
# 스트링화를 하고 빼는 퇴근시간에서 출근시간을 빼는 것보다 분 수로 바꾼다음에 빼는 방식으로 해야 함.
