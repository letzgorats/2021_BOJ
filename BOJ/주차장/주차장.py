import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split()) # 주차 공간, 차량 수 
fare = [0]
for _ in range(N):
    fare.append(int(input())) # 주차공간 번호의 단위무게당 요금
weight = [0]
for _ in range(M):  # 차량 1~M 까지의 무게
    weight.append(int(input()))

enter_order = []
for _ in range(2*M):    # 차량이 들어오고 나가는 출입 리스트 
    enter_order.append(int(input()))

queue = deque(enter_order)
# 1번 자리 부터 N번자리 까지 주차가능한지의 여부와 차 번호를 나타내는 리스트
possible_lot = [[True,0] for _ in range(N+1)] 

answer = 0
wait_for = deque([]) # 주차 공간이 현재 꽉차있을 때 대기하는 차 리스트
while queue:
    car = queue.popleft()   
    wait_queue = True # 대기하는 차가 발생하는지 나타내는 변수
    if car > 0 :    # 차가 들어오는 경우
        for i in range(1,N+1):
            if possible_lot[i][0] == True : # 비어있으면 그 자리 주차
                answer += weight[car] * fare[i] # 그 차의 무게 * 주차공간별 요금
                possible_lot[i][1] = car # 주차장 자리 i번에는 car번째 차가 주차함
                possible_lot[i][0] = False # 해당 자리(i)는 주차 불가를 뜻하는 False로 변경                
                wait_queue = False
                break   
        if wait_queue:  # 대기하는 차가 발생했다면
            wait_for.append(car) # 대기열에 그 차를 넣어준다.
    else:   # 차가 나가는 경우
        car = -car # 음수의 car를 양수로 바꾸고
        for i in range(1,N+1):
            if possible_lot[i][1] == car :
                possible_lot[i][0] = True # 다시 해당 주차자리 주차 가능을 뜻하는 True로 변경
                if len(wait_for) != 0: # 대기열에 차가 있다면
                    car = wait_for.popleft() # 대기하는 앞순 차 들어가게 해준다.
                    possible_lot[i][0] = False # 해당 주차자리 채우고
                    possible_lot[i][1] = car # 해당 주차자리는 그 차가 차지
                    answer += weight[car] * fare[i] # 주차료 계산
                break
print(answer)
