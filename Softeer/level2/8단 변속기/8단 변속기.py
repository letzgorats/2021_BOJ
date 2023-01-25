import sys
input = sys.stdin.readline

degrees = list(map(int,input().split()))
answer = ""

for idx,d in enumerate(degrees[:-1]):
    if d+1 == degrees[idx+1] :
        answer = "ascending"
    elif d-1 == degrees[idx+1] :
        answer = "descending"
    else:
        answer = "mixed"
        break
print(answer)
