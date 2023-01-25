import sys
input = sys.stdin.readline

W, N = map(int,input().split())
have = [(list(map(int,input().split()))) for _ in range(N)]

have = sorted(have,key = lambda x : -x[1])  # 무게당 가격이 높은 순으로 정렬
total = 0 
for h1 in have:
    if W - h1[0] >= 0:
        W -= h1[0]
        total += (h1[0] * h1[1]) 
    else:
        total += W * h1[1]
        break
print(total)
