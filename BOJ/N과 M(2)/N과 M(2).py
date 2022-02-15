import sys
input = sys.stdin.readline
from itertools import permutations,combinations

n,m = map(int,input().split())  # n과 m을 입력받기
answer_list = []  # answer_list 라는 빈 리스트 생성
answer_list = combinations(range(1,n+1),m)  # 1부터 n+1 까지의 수를 m 개의 조합을 모두 answer_list 라 한다.
for i in answer_list: # answer_list 에 있는 모든 조합을 
    print(* i)  # 튜플 형태가 아닌 수 형태로 출력한다.
