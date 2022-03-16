import sys
input = sys.stdin.readline
import heapq 

n = int(input())   # 수업 수 n을 입력받기 
lecture = []  # 강의 리스트 생성
for _ in range(n):  # n을 돌면서,
    start_to_end = list(map(int,input().split())) # start_to_end를 리스트화 하고
    lecture.append(start_to_end)  # lecture에 append해준다.
 
lecture= sorted(lecture, key = lambda x : x[0]) # lecture를 x[0](강의 시작하는 시간)오름차순으로 정렬한다.

start = lecture[0][0] # 맨 처음 시작하는 lecture의 시간은 lecture[0][0] (이거는 문제푸는데에 사용 안됐다.)
min_until = lecture[0][1] # 맨 처음 시작하는 lecture 끝나는 시간은 lecture[0][1]
min_until_list = [min_until]  # min_until_list라는 리스트에 min_until을 넣어주고 시작한다.
heapq.heapify(min_until_list) # heap화 시켜준다.

total = 1 # 강의한개 넣고 시작하니까 total 강의실 개수도 1개로 시작

for x in lecture[1:]: # lecture의 1번째 강의부터 순회하기 시작(맨 처음 강의를 이미 계산한 상태에서 시작한 것이므로)
    if x[0] < min_until_list[0]: # 지금 순회하는 강의의 시작 시간이 min_until_list의 최소값보다 작으면(min_until_list는 힙이기 때문에, 제일 작은 시간이 앞으로 온다.)
        # 강의실 1개 더 추가해야 한다.
        total += 1  
        heapq.heappush(min_until_list,x[1]) # 그리고 지금 순회하는 강의의 끝나는 시간도 역시 집어넣어준다.
    else:   # 시작 시간이 크거나 같으면 빈 강의실이 있다는 것(따로 강의실을 추가해주지 않아도 된다는 것)
        heapq.heappop(min_until_list) # min_until_list의 가장 작은 수를 pop해준다.(맨 앞 값이겠다.)
        heapq.heappush(min_until_list,x[1]) # 그리고 지금 순회하는 강의의 끝나는 시간을 집어넣는다.

print(total)  # 최소로 사용하게 되는 총 강의실 개수 출력
