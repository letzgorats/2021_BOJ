import sys
input = sys.stdin.readline

testcase = int(input())  # 테스트 케이스 입력받기
for _ in range(testcase): # 테스트 케이스 돌면서
    candy , box = map(int,input().split())  # 사탕 개수와 박스 개수 입력받기 
    boxes = []  # boxes 라는 빈 리스트 생성
    for _ in range(box):  # 박스의 개수만큼 돌면서
        r , c = map(int,input().split())  # 각각의 박스의 가로와 세로 길이 입력받기
        boxes.append(r * c) # boxes 라는 리스트에 각각의 박스의 (가로x세로)만큼의 값 추가하기
    # boxes = heapq.heapify(boxes)
    boxes = sorted(boxes,reverse=True)  # 내림차순으로 정렬
    answer = 0  
    for b in boxes: # boxes를 돌면서
        if candy > 0: # candy 값이 양수이면
            candy -= b  # candy에서 각 box의 수용개수만큼 빼면서
            answer += 1   # 사용해야하는 최소 박스의 개수는 하나씩 증가시켜준다.
        else: break # 음수면 빠져나온다.
    print(answer) 
