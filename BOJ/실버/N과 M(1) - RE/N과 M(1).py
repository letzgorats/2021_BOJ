import sys
input = sys.stdin.readline
from itertools import permutations  # 순열 라이브러리 import

N,M = map(int,input().split())  # N과 M 입력받기
number_list = [i for i in range(1,N+1)] # 1부터 N까지의 number_list 생성
answer = list(permutations(number_list,M))  # 그 중에서 중복 없이 M개를 고른 순열 생성하고 리스트화
for x in answer:  # answer리스트에서 x를 그냥 뽑아내면, 튜플형태로 나오므로 추출 필요 
    print(*x)    # 튜플의 모든 값 추출
