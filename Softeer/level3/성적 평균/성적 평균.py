import sys
input = sys.stdin.readline

N, K = map(int,input().split())
S_list = list(map(int,input().split()))
for _ in range(K):
    a,b = map(int,input().split())
    tmp = round(sum(S_list[a-1:b]) / (b-a+1),2)
    print("{0:.2f}".format(tmp))
