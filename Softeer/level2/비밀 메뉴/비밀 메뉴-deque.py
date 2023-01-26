# deque을 사용한 풀이

import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int,input().split())
secret = list(map(int,input().split()))     # 비밀 메뉴가 나오는 버튼 리스트
user_did = list(map(int,input().split()))   # 사용자가 누른 버튼 리스트
start = deque([])

for i in range(N):
    if user_did[i] == secret[0]:    # 사용자가 누른버튼배열 중에 secret 시작 버튼과 같은 위치를 start 리스트에 넣는다.
        start.append(i)

answer = "normal"
while start and answer != "secret": # start 배열이 비어있거나 answer가 secret이면 빠져나오도록 한다.
    s = start.popleft()     # start 배열에서 원소를 뽑는데, 이는 탐색 시작 인덱스를 뜻한다.
    tmp = M                 # tmp라는 변수에 M을 저장하고
    for button in user_did[s:]:     # 사용자가 누른 버튼배열에서 s부터 탐색시작
        if button == secret[M-tmp]:   # 순회하는 버튼이 비밀메뉴가 나오는 버튼배열에 있는 원소와 같다면 (비밀버튼배열은 M개이므로 M-tmp는 0 부터 시작)
            tmp -= 1                # tmp 를 하나씩 뺀다.(그러면, M-tmp 가 0,1,2,...이런식으로 가니까)
            if tmp == 0:            # tmp가 0이 된다면, 비밀버튼배열이 사용자가 누른 버튼배열에 차례대로 다 속해있다는 의미이므로 
                answer = "secret"   # answer을 "secret"으로 바꿔주고 탈출한다.
                break
        else:              # 차례대로 속해있지 않으면, 더 볼필요 없이 다음 start에 속해있는 인덱스부터 순회하러 간다.
            break
print(answer)
