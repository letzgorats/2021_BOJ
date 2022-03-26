import sys
input = sys.stdin.readline
 
N = int(input())    # 센서의 개수 
K = int(input())    # 집중국의 개수
sensor_position = sorted(list(map(int,input().split())))    # 센서의 위치 오름차순
 
distance_list = []	# 모든 센서간의 거리 리스트
for idx,sensor in enumerate(sensor_position[:-1]):	
	# 현재 탐색하고 있는 sensor와 다음 센서(sensor_position[idx+1]간의 거리를 더해준다.)
    distance_list.append(sensor_position[idx+1]-sensor)	
 
# 내림차순 정렬하고 집중국 K개를 설치하므로, K-1개의 구역을
distance_list = sorted(distance_list,reverse=True)[K-1:]    # 큰 것부터 K-1개 슬라이싱(삭제)
 
# 남아있는 거리 리스트의 합이 최소의 집중국 수용범위 합이다.
answer = 0
for d in distance_list:
    answer += d
 
print(answer)
